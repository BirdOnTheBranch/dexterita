<main id="app" class="content">
  <nav class="nav">
    <menu class="nav__controls">
      <icon class="nav__icon" use="#filter"></icon>

      <li v-for="(active, menu) in menus" class="nav__label"
          :class="{
          'nav__label--active' : active,
          'nav__label--filter': activeFilters[menu].length
        }" @click="setMenu(menu, active)">
        {{ menu }}
      </li>

      <li class="nav__label nav__label--clear" @click="clearAllFilters">Clear all</li>
    </menu>

    <label class="nav__label" @click="modal = !modal">About this pen</label>
  </nav>

  <transition-group name="dropdown" tag="section" class="dropdown" :style="dropdown">
    <menu v-for="(options, filter) in filters" class="filters"
          v-show="menus[filter]" ref="menu" :key="filter">

      <li v-if="filter === 'rating'" class="filters__rating">
        <output>
          <label>Minimum rating:&nbsp;</label>
          {{ parseFloat(filters.rating).toFixed(1) }}
        </output>

        <input v-model="filters.rating" class="filters__range" type="range"
               :min="rating.min" :max="rating.max" step="0.1"/>
      </li>

      <template v-else>
        <li v-for="(active, option) in options" class="filters__item"
            :class="{ 'filters__item--active': active }"
            @click="setFilter(filter, option)">
          {{ option }}
        </li>
      </template>
    </menu>
  </transition-group>

  <transition-group name="company" tag="ul" class="content__list">
    <li class="company" v-for="company in list" :key="company.id">
      <div class="company__info">
        <icon class="company__logo" :style="`fill:${company.color}`" :use="company.logo"></icon>
        <h2 class="company__name">{{ company.name }}</h2>
        <blockquote class="company__slogan">{{ company.slogan }}</blockquote>
      </div>

      <ul class="company__details">
        <li class="company__data">
          <label class="company__label">Curso</label>
          <p class="company__country"
             @click="clearFilter('countries', company.country)">
            {{ company.course }}
          </p>
        </li>

        <li class="company__data">
          <label class="company__label">Rating</label>
          <p class="company__rating">{{ company.rating.toFixed(1) }}</p>
        </li>
      </ul>
    </li>
  </transition-group>

  <transition name="modal">
    <section v-if="modal" class="modal" @click="modal = false">
      <article class="modal__content" @click.stop>
        <h4 class="modal__title">For the full tutorial</h4>
        <h4 class="modal__title">that goes with this pen</h4>

        <h5 class="modal__link" @click="modal = false">
          <a href="https://snipcart.com/blog/vuejs-transitions-animations" target="_blank">
            Creating Vue.js Transitions &amp; Animations
          </a>
        </h5>

        <button class="modal__close" @click="modal = false">&times;</button>
      </article>
    </section>
  </transition>
</main>

<script>
export default ({
  components: {
    icon: { template: '<svg><use :xlink:href="use"/></svg>', props: ['use'] },
  },

  data() {
    return {
      modal: false,
      companies: [],
      dropdown: { height: 0 },
      rating: { min: 10, max: 0 },
      filters: {
        countries: {}, categories: {}, rating: 0, subjects: {},
      },
      menus: {
        countries: false, categories: false, rating: false, subjects: false,
      },
    };
  },

  computed: {
    activeMenu() {
      return Object.keys(this.menus).reduce(($$, set, i) => ((this.menus[set]) ? i : $$), -1);
    },

    list() {
      const { countries, categories, subjects } = this.activeFilters;

      return this.companies.filter(({
        subject, country, keywords, rating,
      }) => {
        if (rating < this.filters.rating) return false;
        // eslint-disable-next-line no-bitwise
        if (countries.length && !~countries.indexOf(country)) return false;
        // eslint-disable-next-line no-bitwise
        if (subjects.length && !~subjects.indexOf(subject)) return false;
        // eslint-disable-next-line no-bitwise
        return !categories.length || categories.every((cat) => ~keywords.indexOf(cat));
      });
    },

    activeFilters() {
      const { countries, categories, subjects } = this.filters;

      return {
        countries: Object.keys(countries).filter((c) => countries[c]),
        categories: Object.keys(categories).filter((c) => categories[c]),
        subjects: Object.keys(subjects).filter((c) => subjects[c]),
        rating: (this.filters.rating > this.rating.min) ? [this.filters.rating] : [],
      };
    },
  },

  watch: {
    activeMenu(index, from) {
      if (index === from) return;

      this.$nextTick(() => {
        if (!this.$refs.menu || !this.$refs.menu[index]) {
          this.dropdown.height = 0;
        } else {
          this.dropdown.height = `${this.$refs.menu[index].clientHeight + 16}px`;
        }
      });
    },
  },

  methods: {
    setFilter(filter, option) {
      if (filter === 'countries') {
        this.filters[filter][option] = !this.filters[filter][option];
      } else if (filter === 'subjects') {
        this.filters[filter][option] = !this.filters[filter][option];
      } else {
        setTimeout(() => {
          this.clearFilter(filter, option, this.filters[filter][option]);
        }, 100);
      }
    },

    clearFilter(filter, except, active) {
      if (filter === 'rating') {
        this.filters[filter] = this.rating.min;
      } else {
        Object.keys(this.filters[filter]).forEach((option) => {
          this.filters[filter][option] = except === option && !active;
        });
      }
    },

    clearAllFilters() {
      Object.keys(this.filters).forEach(this.clearFilter);
    },

    setMenu(menu, active) {
      Object.keys(this.menus).forEach((tab) => {
        this.menus[tab] = !active && tab === menu;
      });
    },
  },

  beforeMount() {
    fetch('https://s3-us-west-2.amazonaws.com/s.cdpn.io/450744/mock-data.json')
      .then((response) => response.json())
      .then((companies) => {
        this.companies = companies;

        companies.forEach(({ course, keywords, rating }) => {
          this.$set(this.filters.countries, course, false);

          if (this.rating.max < rating) this.rating.max = rating;
          if (this.rating.min > rating) {
            this.rating.min = rating;
            this.filters.rating = rating;
          }

          keywords.forEach((category) => {
            this.$set(this.filters.categories, category, false);
          });
        });
      });
  },
});

// inject svg spritesheet
fetch('https://s3-us-west-2.amazonaws.com/s.cdpn.io/450744/mock-logos.svg')
  .then((response) => response.text()).then((sprite) => {
    const figure = document.createElement('figure');
    figure.style.display = 'none';
    figure.innerHTML = sprite;
    document.body.insertBefore(figure, document.body.children[0]);
  });
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  html {
    box-sizing: border-box;
    font-size: 100%;
    height: 100%;
    font-family: 'Libre Franklin', sans-serif;
  }
  html.lato {
    font-family: "Lato", sans-serif;
  }
  html.prompt {
    font-family: "Prompt", sans-serif;
  }

  body {
    position: relative;
    height: 100%;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  /* reset */
  * {
    box-sizing: inherit;
    margin: 0;
    padding: 0;
    border-radius: 0;
    border: none;
    outline: none;
    background: none;
    -webkit-margin-before: 0;
    -webkit-margin-after: 0;
    -webkit-margin-start: 0;
    -webkit-margin-end: 0;
    -webkit-padding-before: 0;
    -webkit-padding-start: 0;
    -webkit-padding-end: 0;
    -webkit-padding-after: 0;
  }

  *::before,
  *::after {
    box-sizing: inherit;
  }

  *:active,
  *:hover {
    outline: 0;
  }

  b, i, em, strong,
  h1, h2, h3, h4, h5, h6,
  th, td, pre, ins, del, address,
  input, select, button, textarea {
    text-transform: inherit;
    font-family: inherit;
    font-size: inherit;
    font-weight: normal;
    font-style: normal;
    letter-spacing: inherit;
  }

  textarea,
  input {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background-clip: padding-box;
  }

  a, ins, del, button {
    color: inherit;
    text-decoration: none;
  }

  ul, ol,
  menu {
    list-style: none;
  }

  table,
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
  }

  pre,
  textarea {
    overflow: auto;
    max-width: 100%;
  }

  img {
    width: 100%;
    height: auto;
    display: block;
  }

  svg:not(:root) {
    overflow: hidden;
  }

  form {
    width: 100%;
  }

  button {
    cursor: pointer;
    overflow: visible;
  }

  textarea {
    resize: none;
  }

  input[type='range'] {
    -webkit-appearance: none;
    background-color: transparent;
  }
  input[type='range']::-ms-track {
    cursor: pointer;
    background: transparent;
    border-color: transparent;
    color: transparent;
  }
  input[type='range']::-webkit-slider-thumb {
    -webkit-appearance: none;
  }
  .content {
    position: relative;
    font-family: 'Nunito', sans-serif;
    font-weight: 300;
    color: #3d5358;
    max-width: 780px;
    margin: 0 auto;
  }
  .content__list {
    position: relative;
    margin-top: 1rem;
    padding-right: 1rem;
    padding-bottom: 5rem;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
  }

  .company {
    position: relative;
    width: calc(100% / 2 - 1rem);
    display: inline-flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-pack: justify;
    justify-content: space-between;
    margin-left: 1rem;
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-radius: 6px;
    background-color: white;
    box-shadow: 0 0 0 1px #c5d0d1;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-transform-origin: 10% 50%;
    transform-origin: 10% 50%;
    z-index: 1;
  }
  @media (min-width: 800px) {
    .company {
      width: calc(100% / 3 - 1rem);
    }
  }
  .company-move {
    -webkit-transition: all 600ms ease-in-out 50ms;
    transition: all 600ms ease-in-out 50ms;
  }
  .company-enter-active {
    -webkit-transition: all 300ms ease-out;
    transition: all 300ms ease-out;
  }
  .company-leave-active {
    -webkit-transition: all 200ms ease-in;
    transition: all 200ms ease-in;
    position: absolute;
    z-index: 0;
  }
  .company-enter, .company-leave-to {
    opacity: 0;
  }
  .company-enter {
    -webkit-transform: scale(0.9);
    transform: scale(0.9);
  }
  .company__data {
    line-height: 1.3;
  }
  .company__label {
    font-size: 0.8rem;
  }
  .company__rating {
    text-align: center;
  }
  .company__info {
    padding: 0 0.75rem;
    text-align: center;
  }
  .company__logo {
    width: 3rem;
    height: 3rem;
    margin: 0 auto;
  }
  .company__name {
    height: 2.5rem;
    margin: 0.75rem 0;
    font-size: 1.3rem;
    font-weight: 200;
    text-align: center;
  }
  .company__slogan {
    height: 2rem;
    text-align: center;
    font-weight: 400;
    text-transform: capitalize;
  }
  .company__details {
    display: -webkit-box;
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
    margin-top: 1.5rem;
    padding: 0.5rem 0.75rem;
    background-color: rgba(197, 208, 209, 0.1);
    border-top: 1px solid #c5d0d1;
  }
  .company__country:hover {
    text-decoration: underline;
    cursor: pointer;
  }

  .nav {
    display: -webkit-box;
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    align-items: center;
    white-space: nowrap;
    margin: 0 1rem;
    padding: 2rem 0.5rem 1rem;
    border-bottom: 1px solid #c5d0d1;
  }
  .nav__controls {
    display: -webkit-box;
    display: flex;
  }
  .nav__icon {
    width: 1rem;
    height: 1rem;
    fill: currentColor;
  }
  .nav__label {
    position: relative;
    margin-left: 1rem;
    text-transform: capitalize;
    z-index: 1;
    cursor: pointer;
  }
  .nav__label::after {
    content: '\00d7';
    display: inline-block;
    color: transparent;
    width: 0.5rem;
    font-weight: 400;
    -webkit-transform: scale(0);
    transform: scale(0);
    -webkit-transition: -webkit-transform 150ms ease-in-out;
    transition: -webkit-transform 150ms ease-in-out;
    transition: transform 150ms ease-in-out;
    transition: transform 150ms ease-in-out, -webkit-transform 150ms ease-in-out;
  }
  .nav__label--clear {
    color: #f68185;
    opacity: 0;
    -webkit-transform: translate3d(-25%, 0, 0);
    transform: translate3d(-25%, 0, 0);
    pointer-events: none;
    -webkit-transition: all 275ms ease-in-out;
    transition: all 275ms ease-in-out;
  }
  .nav__label--filter ~ .nav__label--clear {
    opacity: 1;
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    pointer-events: auto;
  }
  .nav__label--filter::after, .nav__label--active::after {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
  .nav__label--filter::after {
    content: '\2022';
    color: #46d2c4;
  }
  .nav__label--active::after {
    content: '\00d7';
    color: #f68185;
  }

  .dropdown {
    position: relative;
    height: 0;
    overflow: hidden;
    -webkit-transition: height 350ms;
    transition: height 350ms;
  }
  .dropdown::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1rem;
    background-image: -webkit-gradient(linear, left bottom, left top,
    from(white), to(rgba(255, 255, 255, 0)));
    background-image: linear-gradient(to top, white, rgba(255, 255, 255, 0));
  }
  .dropdown-enter, .dropdown-leave-to {
    opacity: 0;
  }
  .dropdown-leave, .dropdown-enter-to {
    opacity: 1;
  }
  .dropdown-enter-active, .dropdown-leave-active {
    position: absolute;
    width: 100%;
    -webkit-transition: opacity 200ms ease-in-out;
    transition: opacity 200ms ease-in-out;
  }
  .dropdown-enter-active {
    -webkit-transition-delay: 100ms;
    transition-delay: 100ms;
  }

  .filters {
    padding: 0 1rem;
    display: -webkit-box;
    display: flex;
    flex-wrap: wrap;
    -webkit-box-align: start;
    align-items: flex-start;
  }
  .filters__item {
    margin-top: 0.5rem;
    margin-right: 0.5rem;
    padding: 0.25rem 0.5rem;
    border: 1px solid #c5d0d1;
    border-radius: 6px;
    font-size: 0.8rem;
    line-height: 1.35;
    cursor: pointer;
    -webkit-transition: all 275ms;
    transition: all 275ms;
  }
  .filters__item:hover {
    border-color: #379a93;
  }
  .filters__item--active {
    color: white;
    border-color: #379a93;
    background-color: #379a93;
  }
  .filters__rating {
    width: 100%;
    display: -webkit-box;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-align: center;
    align-items: center;
    padding: 1.5rem 0;
  }
  .filters__range {
    width: 200px;
    margin-top: 1rem;
    color: inherit;
  }
  .filters__range::-webkit-slider-thumb {
    width: 0.8rem;
    height: 0.8rem;
    margin-top: calc(-0.4rem + 2px);
    border-radius: 100%;
    background-color: currentColor;
  }
  .filters__range::-webkit-slider-runnable-track {
    width: 100%;
    height: 4px;
    background-image: -webkit-gradient(linear, left top, right top, from(white), to(#46d2c4));
    background-image: linear-gradient(to right, white, #46d2c4);
  }

  .modal {
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    display: -webkit-box;
    display: flex;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.6);
    z-index: 1;
  }
  .modal-enter-active, .modal-leave-active {
    -webkit-transition: opacity 350ms;
    transition: opacity 350ms;
  }
  .modal-enter, .modal-leave-to {
    opacity: 0;
  }
  .modal-leave, .modal-enter-to {
    opacity: 1;
  }
  .modal__content {
    position: relative;
    display: -webkit-box;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    width: 90%;
    max-width: 500px;
    min-height: 250px;
    padding: 1.5rem 1rem;
    background-color: white;
    border: 1px solid #c5d0d1;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 0.5rem 1.75rem -0.25rem rgba(61, 83, 88, 0.4);
  }
  .modal__title {
    font-weight: 400;
    font-size: 1.5rem;
  }
  .modal__link {
    margin-top: 1.5rem;
    position: relative;
    font-size: 1.2rem;
    font-weight: 300;
    z-index: 0;
  }
  .modal__link::after {
    content: '';
    width: 100%;
    height: 1px;
    position: absolute;
    bottom: 0;
    left: 0;
    background-color: currentColor;
    z-index: -1;
    -webkit-transition: background-color 225ms ease-out;
    transition: background-color 225ms ease-out;
  }
  .modal__link:hover::after {
    background-color: #46d2c4;
  }
  .modal__close {
    position: absolute;
    top: 0.25rem;
    right: 1rem;
    font-size: 1.75rem;
    font-weight: 400;
    opacity: 0.5;
    -webkit-transition: opacity 150ms ease-out;
    transition: opacity 150ms ease-out;
  }
  .modal__close:hover {
    opacity: 1;
  }
</style>
