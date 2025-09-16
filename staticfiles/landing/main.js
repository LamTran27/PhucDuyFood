function sprinkleSpices(sizeClass) {
  const template = document.querySelector('.spice-template');
  if (!template) return;

  const clone = template.cloneNode(true);
  clone.classList.remove('spice-template');
  clone.classList.add('spice-container', sizeClass);
  clone.style.display = 'block';
  document.body.appendChild(clone);

  setTimeout(() => {
    clone.remove();
  }, 3500);
}

// Đợi DOM sẵn sàng trước khi rắc
document.addEventListener("DOMContentLoaded", () => {
  sprinkleSpices('size-large');   // Lần 1: To
  setTimeout(() => sprinkleSpices('size-medium'), 1500); // Lần 2: Vừa
  setTimeout(() => sprinkleSpices('size-small'), 3000);  // Lần 3: Nhỏ
});
