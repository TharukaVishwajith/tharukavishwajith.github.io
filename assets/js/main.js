// Theme toggle, mobile menu, scroll reveal and small article helpers. No dependencies.
(function () {
  var root = document.documentElement;

  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  var menuBtn = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        menuBtn.setAttribute("aria-expanded", "false");
      }
    });
  }

  var reveal = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveal.length) {
    root.classList.add("js-reveal");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveal.forEach(function (el) { io.observe(el); });
  }

  // Article table of contents, built from the h2/h3 headings kramdown gives ids to.
  var toc = document.querySelector("[data-toc]");
  var prose = document.querySelector(".prose");
  if (toc && prose) {
    var heads = prose.querySelectorAll("h2[id], h3[id]");
    if (heads.length < 2) {
      toc.closest(".toc").remove();
    } else {
      heads.forEach(function (h) {
        var li = document.createElement("li");
        li.className = h.tagName === "H3" ? "toc-sub" : "";
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        toc.appendChild(li);
      });
    }
  }

  // Copy buttons on code blocks.
  document.querySelectorAll(".prose div.highlighter-rouge").forEach(function (block) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "copy-btn";
    btn.textContent = "Copy";
    btn.addEventListener("click", function () {
      var code = block.querySelector("code");
      if (!code || !navigator.clipboard) return;
      navigator.clipboard.writeText(code.innerText).then(function () {
        btn.textContent = "Copied";
        setTimeout(function () { btn.textContent = "Copy"; }, 1500);
      });
    });
    block.appendChild(btn);
  });

  // Client-side filter on the "all articles" page.
  var filter = document.querySelector("[data-filter]");
  if (filter) {
    var items = document.querySelectorAll("[data-filter-item]");
    var empty = document.querySelector("[data-filter-empty]");
    filter.addEventListener("input", function () {
      var q = filter.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (item) {
        var hit = !q || item.getAttribute("data-filter-item").indexOf(q) !== -1;
        item.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  }
})();
