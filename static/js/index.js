// $('.btn-toggle').click(function() {
//   $(this).toggleClass('btn-day btn-night');
//   $('body').toggleClass('dark-mode light-mode');
//   $('#gridplus').toggleClass('dark-mode-grid grid-plus');

//   // پاک کردن مقدار theme قبل از ذخیره وضعیت جدید
//   localStorage.removeItem('theme');
//
//   // ذخیره وضعیت دکمه در localStorage
//   if ($(this).hasClass('btn-day')) {
//     localStorage.setItem('theme', 'day');
//   } else {
//     localStorage.setItem('theme', 'night');
//   }
// });
//
//
// $(document).ready(function() {
//   // بررسی وضعیت دکمه در localStorage
//   var theme = localStorage.getItem('theme');
//   if (theme === 'night') {
//     $('.btn-toggle').removeClass('btn-day').addClass('btn-night');
//     $('body').removeClass('light-mode').addClass('dark-mode');
//     $('#gridplus').removeClass('grid-plus').addClass('dark-mode-grid');
//   } else {
//     $('.btn-toggle').removeClass('btn-night').addClass('btn-day');
//     $('body').removeClass('dark-mode').addClass('light-mode');
//   }
// });

