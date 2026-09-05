/* PHASE 5.5-C — Mobile navigation submenu toggle (fixes P1 from PHASE 5.5-B).
   Minimal, dependency-free vanilla JS.
   Only acts at viewport width <= 860px, which is exactly the breakpoint where
   main.css disables the :hover reveal (line 708) and enables the
   .has-children.open reveal (line 709). Desktop hover/focus-within behavior is
   deliberately left untouched. */
(function () {
  'use strict';

  var nav = document.querySelector('.primary-nav');
  if (!nav) return;

  var triggers = nav.querySelectorAll('.has-children > a[aria-haspopup="true"]');
  if (!triggers.length) return;

  var mq = window.matchMedia('(max-width: 860px)');
  var toggle = document.getElementById('nav-toggle');

  // Initialize accessible state for each dropdown trigger.
  for (var i = 0; i < triggers.length; i++) {
    triggers[i].setAttribute('aria-expanded', 'false');
  }

  function closeAll(except) {
    for (var j = 0; j < triggers.length; j++) {
      var li = triggers[j].parentElement;
      if (li === except) continue;
      li.classList.remove('open');
      triggers[j].setAttribute('aria-expanded', 'false');
    }
  }

  for (var k = 0; k < triggers.length; k++) {
    triggers[k].addEventListener('click', function (e) {
      if (!mq.matches) return;            // desktop: leave native hover behavior intact
      e.preventDefault();                  // stop href="#" from jumping to top
      var li = this.parentElement;
      var willOpen = !li.classList.contains('open');
      closeAll(li);                        // accordion: only one submenu open at a time
      li.classList.toggle('open', willOpen);
      this.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
  }

  // Close any open submenu when tapping outside the navigation (mobile only).
  document.addEventListener('click', function (e) {
    if (!mq.matches) return;
    if (nav.contains(e.target)) return;
    closeAll(null);
  }, true);

  // Reset submenu state when the hamburger menu is closed.
  if (toggle) {
    toggle.addEventListener('change', function () {
      if (!this.checked) closeAll(null);
    });
  }
})();
