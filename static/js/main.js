'use strict';

(function ($) {
"use strict";

	/**
   * [isMobile description]
   * @type {Object}
   */
	window.isMobile = {
		Android: function Android() {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function BlackBerry() {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function iOS() {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function Opera() {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function Windows() {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function any() {
			return isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows();
		}
	};
	window.isIE = /(MSIE|Trident\/|Edge\/)/i.test(navigator.userAgent);
	window.windowHeight = window.innerHeight;
	window.windowWidth = window.innerWidth;

	/**
   * Match height
   */
	$('.row-eq-height > [class*="col-"]').matchHeight();

	var resize = debounce(function () {
		$('.row-eq-height > [class*="col-"]').matchHeight();
	}, 250);

	window.addEventListener('resize', resize);

	/**
   * [debounce description]
   * @param  {[type]} func      [description]
   * @param  {[type]} wait      [description]
   * @param  {[type]} immediate [description]
   * @return {[type]}           [description]
   */
	function debounce(func, wait, immediate) {
		var timeout;
		return function () {
			var context = this,
				    args = arguments;
			var later = function later() {
				timeout = null;
				if (!immediate) func.apply(context, args);
			};
			var callNow = immediate && !timeout;
			clearTimeout(timeout);
			timeout = setTimeout(later, wait);
			if (callNow) func.apply(context, args);
		};
	}

	/**
   * Masonry
   */
	$('.grid__inner').masonry({
		itemSelector: '.grid-item',
		columnWidth: '.grid-sizer'
	});

	/**
   * grid css
   */

	$.fn.recalculateWidth = function () {
		var $self = $(this);
		$self.on('recalculateWidth', function () {
			var _self = $(this);
			_self.css('width', '');
			var width = Math.floor(_self.width());
			_self.css('width', width + 'px');
			var height = Math.floor(_self.parent().children('.wide').width() / 2);
			_self.parent().children('.wide').css('height', height + 'px');
		});
		$(window).on('resize', function () {
			$self.trigger('recalculateWidth');
		});
	};

	function work() {
		$('.grid-css').each(function () {
			var workWrapper = $(this),
				    workContainer = $('.grid__inner', workWrapper),
				    filters = $('.filter', workWrapper),
				    filterCurrent = $('.current a', filters),
				    filterLiCurrent = $('.current', filters),
				    duration = 0.3;
			workContainer.imagesLoaded(function () {

				// Fix Height
				if (workWrapper.hasClass('grid-css--fixheight')) {
					workContainer.find('.grid-item__content-wrapper').matchHeight();
				}

				workContainer.isotope({
					layoutMode: 'masonry',
					itemSelector: '.grid-item',
					transitionDuration: duration + 's',
					masonry: {
						columnWidth: '.grid-sizer'
					}
					// hiddenStyle: {},
					// visibleStyle: {}
				});
			});
			filters.on('click', 'a', function (e) {
				e.preventDefault();
				var $el = $(this);
				var selector = $el.attr('data-filter');
				filters.find('.current').removeClass('current');
				$el.parent().addClass('current');
				workContainer.isotope({
					filter: selector
				});
			});

			filters.find('.select-filter').change(function () {
				var $el = $(this);
				var selector = $el.val();
				workContainer.isotope({
					filter: selector
				});
			});

			$('.grid-item', workWrapper).recalculateWidth();
		});
	}
	work();

	/**
  * Footer
  */
	$('#back-to-top').on('click', function (e) {
		e.preventDefault();
		$('html,body').animate({
			scrollTop: 0
		}, 700);
	});

	//*
	// Header
	//*
	var wh = $(window).height(),
		    half = wh / 2,
		    headerHeight = $('header').outerHeight();

	$(window).scroll(function () {
		var scrollTop = $(window).scrollTop();

		if (scrollTop >= half) {
			$('header').addClass('is-scroll');
		} else {
			$('header').removeClass('is-scroll');
		}
	});

	$('.onepage-nav').dropdownMenu({
		menuClass: 'onepage-menu',
		breakpoint: 1200,
		toggleClass: 'active',
		classButtonToggle: 'navbar-toggle',
		subMenu: {
			class: 'sub-menu',
			parentClass: 'menu-item-has-children',
			toggleClass: 'active'
		}
	});

	$('.onepage-nav').onePageNav({
		currentClass: 'current-menu-item',
		scrollOffset: headerHeight
	});

	$(document).ready(function () {
		$('.header__lang_box').hide();
		$('.header__lang > a').click(function (e) {
			e.preventDefault();
			$(this).next().slideToggle();
		});
	});

	//*
	// Back to top
	//*

	$(window).scroll(function () {
		var wh = $(window).height(),
			    scrollTop = $(window).scrollTop();

		if (scrollTop >= wh) {
			$('#back-to-top').addClass('is-visible');
		} else {
			$('#back-to-top').removeClass('is-visible');
		}
	});
})(jQuery);
