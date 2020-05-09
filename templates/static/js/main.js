$(document).ready(function () {

  // Scroll spee
  $('.scroll').on('click','a', function (event) {
    event.preventDefault();
    var id  = $(this).attr('href'),
      top = $(id).offset().top;
      $('body,html').animate({scrollTop: top}, 800);
  });

  // Nav
  $('.navbar-toggle').click(function () {
    $(this).toggleClass('active');
    $('.nav').toggleClass('open');
    $('.wrapper').toggleClass('no-scroll');
    $('.mobile-panel').fadeToggle();
  });

  if($(window).width() < 1200){
    $('.nav__item_drop .nav__link').click(function(e) {
      e.preventDefault();
      $(this).parents('.nav__item_drop').toggleClass('nav__item_drop_active');
      $(this).next('.navdrop').slideToggle( "slow", function() {});
    });
  }

  $(document).click(function(event) {
    if ($(event.target).closest('.navbar-toggle').length 
      || $(event.target).closest('.nav').length ) return;
      $('.navbar-toggle').removeClass('active');
      $('.nav').removeClass('open');
      $('.wrapper').removeClass('no-scroll');
      $('.mobile-panel').fadeIn();
      event.stopPropagation();
  });

  // Search
  $('.btn-search').click(function() {
    $('.modal_search').fadeIn();
  });

  // Modal close
  $('.modal__close').click(function() {
    $('.modal').fadeOut();
  });

  // Tabs
  $('.tabs-js .tabs__item').not(':first').hide();
  $('.tabs-js .tabs__name').click(function() {
    $('.tabs-js .tabs__name').removeClass('active').eq($(this).index()).addClass('active');
    $('.tabs-js .tabs__item').hide().eq($(this).index()).fadeIn()
  }).eq(0).addClass('active');

  // Catalog
  if($(window).width() < 992){
    $('.aside__item h3').click(function() {
      $(this).toggleClass('active');
      $(this).next('.aside__list').slideToggle( "slow", function() {});
    });
  }

  // Maskedinput
  $(function($){
    $('.phone-mask').mask(('+7 ') + '(999) 999-99-99');
  });

  // Accardion
  var accordion = function() {
    var data = $('.accordion').attr('data-accordion')
    $('.accordion-header').on('click', function(){
      $(this).next('.accordion-body').not(':animated').slideToggle()
    })
    $('.accordion-header').click(function () {
      $(this).toggleClass('active');
    });
  }
  accordion();

  // Trust sl
  $('.trust__sl').slick({
    arrows: false,
    autoplay: true,
    slidesToShow: 7,
    slidesToScroll: 5,
    autoplaySpeed: 3000,
    dots: true,
    responsive: [
      {
        breakpoint: 1366,
        settings: {
          slidesToShow: 6
        }
      },{
        breakpoint: 1200,
        settings: {
          slidesToShow: 5
        }
      },{
        breakpoint: 992,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 4
        }
      },{
        breakpoint: 768,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3
        }
      },{
        breakpoint: 576,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },{
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: true,
          prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M0.184,10.586 L9.552,1.144 C9.773,0.922 10.127,0.922 10.347,1.144 C10.568,1.366 10.568,1.723 10.347,1.945 L1.379,10.984 L10.347,20.023 C10.568,20.245 10.568,20.601 10.347,20.823 C10.239,20.932 10.093,20.991 9.952,20.991 C9.810,20.991 9.665,20.936 9.557,20.823 L0.189,11.383 C-0.033,11.164 -0.033,10.803 0.184,10.586 Z"/></svg></button>',
          nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M10.848,10.586 L1.480,1.144 C1.259,0.922 0.905,0.922 0.684,1.144 C0.464,1.366 0.464,1.723 0.684,1.945 L9.653,10.984 L0.684,20.023 C0.464,20.245 0.464,20.601 0.684,20.823 C0.792,20.932 0.939,20.991 1.080,20.991 C1.221,20.991 1.367,20.936 1.475,20.823 L10.843,11.383 C11.064,11.164 11.064,10.803 10.848,10.586 Z"/></svg></button>'
        }
      }
    ]
  });

  // Reviews sl
  $('.reviews__sl').slick({
    arrows: false,
    autoplay: true,
    swipe: false,
    slidesToShow: 4,
    autoplaySpeed: 3000,
    dotsClass: 'slick-dots container',
    dots: true,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          swipe: true,
          slidesToShow: 1,
          adaptiveHeight: true
        }
      }
    ]
  });

  // Product sl small
  $('.product__sl__small').slick({
    arrows: true,
    swipe: false,
    vertical: true,
    autoplay: false,
    slidesToShow: 3,
    centerMode: true,
    focusOnSelect: true,
    centerPadding: '0',
    autoplaySpeed: 3000,
    asNavFor: '.product__sl__big',
    prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M9.602,0.153 L0.175,9.520 C-0.047,9.741 -0.047,10.095 0.175,10.316 C0.397,10.536 0.753,10.536 0.975,10.316 L10.000,1.347 L19.024,10.316 C19.246,10.536 19.602,10.536 19.824,10.316 C19.933,10.208 19.992,10.061 19.992,9.920 C19.992,9.779 19.937,9.633 19.824,9.525 L10.398,0.157 C10.180,-0.064 9.820,-0.064 9.602,0.153 Z"/></svg></button>',
    nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M9.602,10.816 L0.175,1.448 C-0.047,1.227 -0.047,0.873 0.175,0.652 C0.397,0.432 0.753,0.432 0.975,0.652 L10.000,9.621 L19.024,0.652 C19.246,0.432 19.602,0.432 19.824,0.652 C19.933,0.761 19.992,0.907 19.992,1.048 C19.992,1.190 19.937,1.335 19.824,1.443 L10.398,10.811 C10.180,11.032 9.820,11.032 9.602,10.816 Z"/></svg></button>',
    dots: false,
    responsive: [
      // {
      //   breakpoint: 1366,
      //   settings: {
      //     slidesToShow: 6
      //   }
      // }
    ]
  });

  // Product sl big
  $('.product__sl__big').slick({
    swipe: false,
    arrows: false,
    autoplay: false,
    slidesToShow: 1,
    autoplaySpeed: 3000,
    asNavFor: '.product__sl__small',
    dots: false,
    responsive: [
      // {
      //   breakpoint: 1366,
      //   settings: {
      //     slidesToShow: 6
      //   }
      // }
    ]
  });

  // Similar sl
  $('.similar__sl').slick({
    arrows: true,
    autoplay: false,
    slidesToShow: 4,
    autoplaySpeed: 3000,
    dots: false,
    prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M0.184,10.586 L9.552,1.144 C9.773,0.922 10.127,0.922 10.347,1.144 C10.568,1.366 10.568,1.723 10.347,1.945 L1.379,10.984 L10.347,20.023 C10.568,20.245 10.568,20.601 10.347,20.823 C10.239,20.932 10.093,20.991 9.952,20.991 C9.810,20.991 9.665,20.936 9.557,20.823 L0.189,11.383 C-0.033,11.164 -0.033,10.803 0.184,10.586 Z"/></svg></button>',
    nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M10.848,10.586 L1.480,1.144 C1.259,0.922 0.905,0.922 0.684,1.144 C0.464,1.366 0.464,1.723 0.684,1.945 L9.653,10.984 L0.684,20.023 C0.464,20.245 0.464,20.601 0.684,20.823 C0.792,20.932 0.939,20.991 1.080,20.991 C1.221,20.991 1.367,20.936 1.475,20.823 L10.843,11.383 C11.064,11.164 11.064,10.803 10.848,10.586 Z"/></svg></button>',
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          swipe: true,
          slidesToShow: 3,
        }
      },{
        breakpoint: 992,
        settings: {
          swipe: true,
          slidesToShow: 2,
        }
      },{
        breakpoint: 768,
        settings: {
          swipe: true,
          slidesToShow: 1,
        }
      }
    ]
  });

  // Article sl
  $('.article__sl').slick({
    arrows: true,
    autoplay: true,
    slidesToShow: 1,
    autoplaySpeed: 3000,
    dots: false,
    responsive: [
      // {
      //   breakpoint: 1366,
      //   settings: {
      //     slidesToShow: 6
      //   }
      // }
    ]
  });

});

// Map
// ymaps.ready(init);
// var myMap, 
//     myPlacemark;

// function init(){ 
//   myMap = new ymaps.Map("map", {
//     center: [55.77511086, 37.61463844],
//     zoom: 16,
//     controls: ['zoomControl']
//   });
  
//   myPlacemark = new ymaps.Placemark([55.77511086, 37.61463844], {});
  
//   myMap.geoObjects.add(myPlacemark);
//   myMap.behaviors.disable([
//     'drag',
//     'scrollZoom'
//   ]);

// }