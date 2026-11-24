(() => {
  const elements = Array.from(document.querySelectorAll(".reveal"));
  if (!elements.length) return;

  const reveal = (element) => element.classList.add("is-visible");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reduceMotion || !("IntersectionObserver" in window)) {
    elements.forEach(reveal);
    return;
  }

  elements.forEach((element, index) => {
    element.style.transitionDelay = `${Math.min(index % 4, 3) * 65}ms`;
  });

  // Lo que ya está en pantalla se muestra sin esperar al observer: pestañas en
  // segundo plano, capturas, prerender y crawlers también ven el contenido.
  const revealInView = () => {
    const limit = window.innerHeight - 35;
    elements.forEach((element) => {
      if (element.classList.contains("is-visible")) return;
      if (element.getBoundingClientRect().top < limit) reveal(element);
    });
  };

  let delivered = false;
  const observer = new IntersectionObserver((entries, currentObserver) => {
    delivered = true;
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      reveal(entry.target);
      currentObserver.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });

  elements.forEach((element) => observer.observe(element));

  revealInView();
  window.addEventListener("load", revealInView);
  window.addEventListener("resize", revealInView);
  document.addEventListener("visibilitychange", revealInView);

  // Red de seguridad: si el observer nunca entrega (pestaña oculta, prerender,
  // captura de página completa), el contenido se muestra igualmente.
  window.setTimeout(() => {
    if (!delivered || document.visibilityState === "hidden") elements.forEach(reveal);
  }, 1500);
})();
