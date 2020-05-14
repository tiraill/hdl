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
      // e.preventDefault();
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

  // Modal bell
  $('.open-modal-bell').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Заказать звонок!');
    modal.find('#id_additional_info').val('Обратный звонок');
    modal.fadeIn();
  });

  // Modal request
  $('.open-modal-request').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Оставьте заявку для сотрудничества!');
    modal.find('#id_additional_info').val('Заявка для сотрудничества');
    modal.fadeIn();
  });

  // Modal consult
  $('.open-modal-consult').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Получите консультацию!');
    modal.find('#id_additional_info').val('Заявка для получения консультации');
    modal.fadeIn();
  });

  // Modal education general
  $('.open-modal-education-general').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Заявка на обучение');
    modal.find('#id_additional_info').val('Заявка на обучение');
    modal.fadeIn();
  });

  // Modal education general-buspro
  $('.open-modal-education-general-buspro').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Заявка на обучение протоколу BusPro');
    modal.find('#id_additional_info').val('Заявка на обучение протоколу BusPro');
    modal.fadeIn();
  });

  // Modal education general-knx
  $('.open-modal-education-general-knx').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Заявка на обучение протоколу KNX');
    modal.find('#id_additional_info').val('Заявка на обучение протоколу KNX');
    modal.fadeIn();
  });

  // Modal education general-online
  $('.open-modal-education-general-online').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Заявка на онлайн курс HDL BusPro');
    modal.find('#id_additional_info').val('Заявка на онлайн курс HDL BusPro');
    modal.fadeIn();
  });

  // Modal education buspro
  $('.open-modal-education-buspro').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Зарегистрироваться на обучение');
    modal.find('#id_additional_info').val('Заявка на обучение');
    modal.fadeIn();
  });

  // Modal education knx
  $('.open-modal-education-knx').click(function(e) {
    e.preventDefault();
    let modal = $('.modal_bell');
    modal.find('h2').text('Купить со скидкой курс сертификации KNX');
    modal.find('#id_additional_info').val('Заявка на покупку со скидкой курса сертификации KNX');
    modal.fadeIn();
  });

  $(document).click(function(event) {
    if ($(event.target).closest('.modal__box').length 
      || $(event.target).closest('.modal_search').length
      || $(event.target).closest('.open-modal-bell').length
      || $(event.target).closest('.open-modal-request').length
      || $(event.target).closest('.open-modal-consult').length
      || $(event.target).closest('.open-modal-education-general').length
      || $(event.target).closest('.open-modal-education-general-buspro').length
      || $(event.target).closest('.open-modal-education-general-knx').length
      || $(event.target).closest('.open-modal-education-general-online').length
      || $(event.target).closest('.open-modal-education-buspro').length
      || $(event.target).closest('.open-modal-education-knx').length
      || $(event.target).closest('.btn-search').length ) return;
      $('.modal').fadeOut();
      event.stopPropagation();
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

  // Keys sl
  const
  slidesCount = $('.keys__sl').find('.keys__sl__item').length,
  $nav = $('.indicator'),
  $navInner = $nav.find('.indicator__inner');

  function updateNav(slide) {
    $navInner.width(`${$nav.width() * (slide + 1) / slidesCount}px`);
  }

  $('.indicator').on('click', function(e) {
    $('.keys__sl').slick('slickGoTo', e.offsetX / $nav.width() * slidesCount | 0);
  });

  $('.keys__sl').on({
    init(e, slick) {
      updateNav(slick.currentSlide);
    },
    beforeChange(e, slick, currentSlide, nextSlide) {
      updateNav(nextSlide);
    },
  }).slick({
    arrows: false,
    autoplay: true,
    slidesToShow: 5,
    autoplaySpeed: 3000,
    dots: false,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 4
        }
      },{
        breakpoint: 992,
        settings: {
          slidesToShow: 3
        }
      },{
        breakpoint: 768,
        settings: {
          arrows: true,
          slidesToShow: 2,
          prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><filter filterUnits="userSpaceOnUse" id="Filter_0" x="0px" y="0px" width="24px" height="34px"  ><feOffset in="SourceAlpha" dx="0" dy="4" /><feGaussianBlur result="blurOut" stdDeviation="2.646" /><feFlood flood-color="rgb(96, 17, 179)" result="floodOut" /><feComposite operator="atop" in="floodOut" in2="blurOut" /><feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#Filter_0)"><path fill-rule="evenodd" d="M6.184,12.586 L15.552,3.144 C15.773,2.922 16.127,2.922 16.347,3.144 C16.568,3.366 16.568,3.723 16.347,3.945 L7.378,12.984 L16.347,22.022 C16.568,22.245 16.568,22.601 16.347,22.824 C16.239,22.932 16.093,22.991 15.952,22.991 C15.810,22.991 15.665,22.937 15.557,22.824 L6.188,13.382 C5.967,13.164 5.967,12.804 6.184,12.586 Z"/></g></svg></button>',
          nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><filter filterUnits="userSpaceOnUse" id="Filter_1" x="0px" y="0px" width="25px" height="34px"><feOffset in="SourceAlpha" dx="0" dy="4" /><feGaussianBlur result="blurOut" stdDeviation="2.646" /><feFlood flood-color="rgb(96, 17, 179)" result="floodOut" /><feComposite operator="atop" in="floodOut" in2="blurOut" /><feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#Filter_1)"><path fill-rule="evenodd" d="M16.848,12.586 L7.480,3.144 C7.259,2.922 6.905,2.922 6.684,3.144 C6.464,3.366 6.464,3.723 6.684,3.945 L15.653,12.984 L6.684,22.022 C6.464,22.245 6.464,22.601 6.684,22.824 C6.792,22.932 6.939,22.991 7.080,22.991 C7.221,22.991 7.367,22.937 7.475,22.824 L16.843,13.382 C17.064,13.164 17.064,12.804 16.848,12.586 Z"/></g></svg></button>',
        }
      },{
        breakpoint: 480,
        settings: {
          arrows: true,
          slidesToShow: 1,
          prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><filter filterUnits="userSpaceOnUse" id="Filter_0" x="0px" y="0px" width="24px" height="34px"  ><feOffset in="SourceAlpha" dx="0" dy="4" /><feGaussianBlur result="blurOut" stdDeviation="2.646" /><feFlood flood-color="rgb(96, 17, 179)" result="floodOut" /><feComposite operator="atop" in="floodOut" in2="blurOut" /><feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#Filter_0)"><path fill-rule="evenodd" d="M6.184,12.586 L15.552,3.144 C15.773,2.922 16.127,2.922 16.347,3.144 C16.568,3.366 16.568,3.723 16.347,3.945 L7.378,12.984 L16.347,22.022 C16.568,22.245 16.568,22.601 16.347,22.824 C16.239,22.932 16.093,22.991 15.952,22.991 C15.810,22.991 15.665,22.937 15.557,22.824 L6.188,13.382 C5.967,13.164 5.967,12.804 6.184,12.586 Z"/></g></svg></button>',
          nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><filter filterUnits="userSpaceOnUse" id="Filter_1" x="0px" y="0px" width="25px" height="34px"><feOffset in="SourceAlpha" dx="0" dy="4" /><feGaussianBlur result="blurOut" stdDeviation="2.646" /><feFlood flood-color="rgb(96, 17, 179)" result="floodOut" /><feComposite operator="atop" in="floodOut" in2="blurOut" /><feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#Filter_1)"><path fill-rule="evenodd" d="M16.848,12.586 L7.480,3.144 C7.259,2.922 6.905,2.922 6.684,3.144 C6.464,3.366 6.464,3.723 6.684,3.945 L15.653,12.984 L6.684,22.022 C6.464,22.245 6.464,22.601 6.684,22.824 C6.792,22.932 6.939,22.991 7.080,22.991 C7.221,22.991 7.367,22.937 7.475,22.824 L16.843,13.382 C17.064,13.164 17.064,12.804 16.848,12.586 Z"/></g></svg></button>',
        }
      }
    ]
  });

  // Realization sl
  $('.realization__sl').slick({
    arrows: true,
    autoplay: true,
    slidesToShow: 1,
    autoplaySpeed: 3000,
    dots: false,
    adaptiveHeight: true,
    prevArrow: '<button class="slick-prev"><svg xmlns="http://www.w3.org/2000/svg"xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M0.469,12.302 L11.965,0.795 C12.169,0.591 12.500,0.591 12.704,0.795 C12.908,0.999 12.908,1.331 12.704,1.535 L1.577,12.671 L12.704,23.807 C12.907,24.011 12.907,24.343 12.704,24.547 C12.601,24.648 12.467,24.700 12.334,24.700 C12.200,24.700 12.066,24.648 11.965,24.547 L0.469,13.041 C0.265,12.837 0.265,12.506 0.469,12.302 Z"/></svg></button>',
    nextArrow: '<button class="slick-next"><svg xmlns="http://www.w3.org/2000/svg"xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" d="M12.531,12.302 L1.035,0.795 C0.831,0.591 0.500,0.591 0.296,0.795 C0.092,0.999 0.092,1.331 0.296,1.535 L11.423,12.671 L0.296,23.807 C0.092,24.011 0.092,24.343 0.296,24.547 C0.399,24.648 0.532,24.700 0.666,24.700 C0.800,24.700 0.934,24.648 1.035,24.547 L12.531,13.041 C12.734,12.837 12.734,12.506 12.531,12.302 Z"/></svg></button>',
    responsive: [
      // {
      //   breakpoint: 1366,
      //   settings: {
      //     slidesToShow: 6
      //   }
      // }
    ]
  });

  // Gallery sl
  $('.gallery__sl').slick({
    arrows: false,
    autoplay: true,
    slidesToShow: 4,
    autoplaySpeed: 5000,
    dots: false,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3
        }
      },{
        breakpoint: 768,
        settings: {
          slidesToShow: 2
        }
      }
    ]
  });

  // Showroom sl
  $('.showroom__sl').slick({
    arrows: false,
    autoplay: true,
    slidesToShow: 3,
    autoplaySpeed: 2000,
    dots: false,
    responsive: [
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2
        }
      },{
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
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