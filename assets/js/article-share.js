// Direct social links work without JavaScript. Enhance copy and device sharing.
(function () {
  document.querySelectorAll('[data-article-share]').forEach(function (section) {
    var url = section.dataset.shareUrl;
    var title = section.dataset.shareTitle;
    var copy = section.querySelector('[data-copy-link]');
    var native = section.querySelector('[data-native-share]');
    var status = section.querySelector('[data-share-status]');
    var input = section.querySelector('[data-share-link]');

    function showLink() {
      input.value = url;
      input.hidden = false;
      input.focus();
      input.select();
      status.textContent = section.dataset.copyHelp;
    }

    copy.hidden = false;
    copy.addEventListener('click', async function () {
      status.textContent = '';
      try {
        if (!navigator.clipboard || typeof navigator.clipboard.writeText !== 'function') {
          showLink();
          return;
        }
        await navigator.clipboard.writeText(url);
        input.hidden = true;
        status.textContent = section.dataset.copied;
      } catch (error) {
        showLink();
      }
    });

    if (typeof navigator.share === 'function') {
      native.hidden = false;
      native.addEventListener('click', async function () {
        status.textContent = '';
        try {
          await navigator.share({ title: title, url: url });
        } catch (error) {
          if (!error || error.name !== 'AbortError') showLink();
        }
      });
    }
  });
})();
