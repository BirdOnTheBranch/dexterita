<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info" sticky>
      <b-navbar-brand href="#">UnedTest</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Exámenes</b-nav-item>
          <b-nav-item href="#">Recursos</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-nav-item @click="modal = !modal">Autor</b-nav-item>
          </b-nav-form>
<!--          <b-nav-form>-->
<!--            <b-form-input size="sm" class="mr-sm-2" placeholder="Atención, Memoria...">-->
<!--            </b-form-input>-->
<!--            <b-button size="sm" class="my-2 my-sm-0" type="submit">Buscar</b-button>-->
<!--          </b-nav-form>-->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

  <main id="app" class="content">
    <div v-if="!started">
      <transition-group name="company2" tag="ul" class="content__list">
        <li class="curso"
            v-for="curso in cursos"
            @click="chooseCurso(curso)"
            :key="curso.id"
        :class="curso.id">
          <div class="company__info">
            <icon class="company__logo" :style="`fill:${curso.color}`" :use="curso.logo"></icon>
            <h2 class="company__name">{{ curso.name }}</h2>
            <blockquote class="company__slogan">{{ curso.slogan }}</blockquote>
            <blockquote class="company__label">{{ curso.week }}</blockquote>
          </div>
        </li>
      </transition-group>
    </div>
    <div v-if="started && !chosenAsignatura">
      <transition-group name="company3" tag="ul" class="content__list">
        <li class="company"
            v-for="asignatura in activeAsignaturas"
            @click="chooseAsignatura(asignatura)"
            :key="asignatura.id">
          <div class="company__info">
            <icon class="company__logo" :style="`fill:${asignatura.color}`" :use="asignatura.logo">
            </icon>
            <h2 class="company__name">{{ asignatura.name }}</h2>
            <blockquote class="company__slogan">{{ asignatura.cuatrimestre }}</blockquote>
          </div>

          <ul class="company__details" :class="currentCurso">

            <li class="company__data" style="margin: 0 auto;">
              <label class="company__label" style="font-size: 0.8em">
                {{ asignatura.credits }} créditos</label>
            </li>
          </ul>
        </li>
      </transition-group>
    </div>
    <div v-if="chosenAsignatura">
      <input class="variation" id="bluepurple" type="radio" value="1" name="color"/>
      <label for="bluepurple"></label>
      <input class="variation" id="sunset" type="radio" value="2" name="color"/>
      <label for="sunset"></label>
      <input class="variation" id="godiva" type="radio" value="3" name="color"/>
      <label for="godiva"></label>
      <input class="variation" id="dark" type="radio" value="4" name="color"
             checked="checked"/>
      <label for="dark"></label>
      <input class="variation" id="pinkaru" type="radio" value="5" name="color"/>
      <label for="pinkaru"></label>
      <main>
        <section>
          <div class="profile profile-long" style="display: inherit">
<!--            <div class="profile__image">-->
<!--              <img :src="currentAsignatura.imagesrc" alt="Foto"/></div>-->
            <div class="profile__info">
              <h3>{{ currentAsignatura.name }}</h3>
              <p v-if="chosenSubject" class="profile__info__extra">Test - {{examDate}}</p>
            </div>
            <!--        Exámenes-->
            <div v-if="chosenSection && chosenSection ==='examenes'">
              <section>
                  <div v-if="!chosenSubject">
                    <transition-group name="dropdown" tag="section" class="dropdown"
                                      :style="dropdown">
                      <menu v-for="(_, filter) in filters" class="filters"
                            v-show="filter === 'convocatoria' && menus[filter]"
                            ref="menu" :key="filter">

                        <li v-if="filter === 'convocatoria'" class="filters__convocatoria">
                          <output>
                            <label>Desde el año:&nbsp;</label>
                            20{{ filters.convocatoria }}
                          </output>

                          <input v-model="filters.convocatoria" class="filters__range" type="range"
                                 :min="convocatoria.min" :max="convocatoria.max" step="1"/>
                        </li>
                      </menu>
                    </transition-group>
                      <div>
                        <table class="lista__curso">
                          <thead>
                          <tr>
                            <th class="tema_title">Autoevaluación</th>
                            <th></th>
                            <th class="table_right"></th>
                          </tr>
                          </thead>
                          <tbody>
                          <tr
                            v-for="company in temaslist"
                            @click="chooseSubject(company.subject, company)"
                            :key="company.id"
                            class="tema_lista"
                          >
                            <td>{{ company.name }}</td>
                            <td>{{ company.slogan }}</td>
                            <td class="table_right">{{ company.questions }}</td>
                          </tr>
                          </tbody>
                        </table>
                      </div>
                      <div>
                        <table class="lista__curso">
                          <thead>
                          <tr>
                            <th class="tema_title_wrap">Exámenes</th>
                            <th class="table_right"></th>
                          </tr>
                          </thead>
                          <tbody>
                          <tr
                            v-for="company in exameneslist"
                            @click="chooseSubject(company.subject, company)"
                            :key="company.id"
                            class="tema_lista"
                          >
                            <td>{{ company.slogan }}</td>
                            <td class="table_right">{{ company.questions }}</td>
                          </tr>
                          </tbody>
                        </table>
                      </div>
<!--                    <transition-group-->
<!--                      v-if="!chosenSubject" name="company" tag="ul" class="content__list">-->

<!--                      <li class="company"-->
<!--                          v-for="company in list"-->
<!--                          @click="chooseSubject(company.subject, company)"-->
<!--                          :key="company.id">-->
<!--                        <div class="company__info">-->
<!--                          <icon class="company__logo"-->
<!--                                :style="`fill:${company.color}`" :use="company.logo">-->
<!--                          </icon>-->
<!--                          <h2 class="company__name">{{ company.name }}</h2>-->
<!--                     <blockquote class="company__slogan">{{ company.slogan }}</blockquote>-->
<!--                          <blockquote class="company__label">{{ company.week }}</blockquote>-->
<!--                        </div>-->

<!--                        <ul class="company__details">-->
<!--                          <li class="company__data">-->
<!--                            <label class="company__label">Curso</label>-->
<!--                            <p class="company__subject">-->
<!--                              {{ company.course_dg }}º-->
<!--                            </p>-->
<!--                          </li>-->

<!--                          <li class="company__data">-->
<!--                       <label class="company__label">{{ company.minutes }}:00 minutos</label>-->
<!--                            <p class="company__rating">{{ company.questions }} Preguntas</p>-->
<!--                          </li>-->
<!--                        </ul>-->
<!--                      </li>-->
<!--                    </transition-group>-->
                  </div>
                  <div v-show="chosenSubject">
                    <h2 v-if="!chosenQuiz" class="testTime">Elige el número de preguntas</h2>
                    <transition-group
                      v-if="!chosenQuiz" name="quizoptions" tag="ul" class="content__list">
                      <li class="company"
                          v-for="opt in quizOptions"
                          @click="chooseOptions(opt)"
                          :key="opt.id"
                          :class="opt.id"
                      >
                        <div class="company__info">
                          <h2
                            v-if="opt.id === 'all'" class="company__name"
                          >Todas ({{ opt.subjectQuestions }})</h2>
                          <h2
                            v-if="opt.id !== 'all'" class="company__name"
                          >{{ opt.subjectQuestions }}</h2>
                        </div>
                      </li>
                    </transition-group>
                  </div>
                  <div v-if="chosenQuiz">
                    <!--container-->
                    <transition name="main_transition">
                      <section class="container">

                        <!--questionBox-->

                        <div class="questionBox">

                          <!-- transition -->
                          <transition :duration="{ enter: 500, leave: 300 }"
                                      enter-active-class="animated zoomIn"
                                      leave-active-class="animated zoomOut"
                                      mode="out-in">

                            <!--questionContainer-->
                            <div class="questionContainer"
                                 v-if="chosenQuiz && questionIndex<quiz.questions.length"
                                 v-bind:key="questionIndex">

                              <header>
                                <!--progress-->
                                <div class="progressContainer">
                                  <div class="progress">
                                    <div class="progress-bar bg-success" role="progressbar"
                                         :style="{ width: (corrects/quiz.questions.length)*100+'%'}"
                                         aria-valuemin="0" aria-valuemax="100">{{corrects}}</div>
                                    <div class="progress-bar bg-danger" role="progressbar"
                                         :style="{width:(incorrects/quiz.questions.length)*100+'%'}"
                                         aria-valuemin="0" aria-valuemax="100">{{incorrects}}</div>
                                  </div>
                                  <p>{{questionIndex+1}} de {{quiz.questions.length}} preguntas</p>
                                  <p>Tiempo restante: {{timeLeft}}</p>
                                </div>
                                <!--/progress-->
                              </header>
                              <!--quizFooter: navigation and progress-->
                              <footer class="questionFooter">
                                <!--pagination-->
                                <nav class="pagination" role="navigation" aria-label="pagination">

                                  <!-- back button -->
                                  <a class="btn btn-light"
                                     v-on:click="prev()"
                                     :disabled="questionIndex < 1">
                                    Anterior
                                  </a>

                                  <!-- next button -->
                                  <a class="btn btn-light" v-on:click="next()"
                                     :disabled="questionIndex===quiz.questions.length">
                                    {{ (userResponses[questionIndex]==null)?'Saltar pregunta':
                                    'Siguiente' }}
                                  </a>

                                </nav>
                                <!--/pagination-->

                              </footer>
                              <!--/quizFooter-->

                              <!-- questionTitle -->
                              <div v-if="quiz.questions[questionIndex].imagen" id='imagen'>
                                <img :src=quiz.questions[questionIndex].imagen />
                              </div>
                              <p class="titleContainer title"
                                 v-html="quiz.questions[questionIndex].text"></p>
<!--                              <div class="titleDate"-->
<!--                                   v-if="quiz.questions[questionIndex].fecha">-->
<!--                                {{ quiz.questions[questionIndex].fecha.mes }} - -->
<!--                                {{ quiz.questions[questionIndex].fecha.year }}-->
<!--                              </div>-->

                              <!-- quizOptions -->
                              <div class="optionContainer">
                                <div class="option"
                                     v-for="(response, index)
                          in quiz.questions[questionIndex].responses"
                                     @click="selectOption(index, response)"
                                     :class="{ 'is-correct':
                              userResponses[questionIndex] === index
                              && response.correct,
                              'is-wrong':
                              userResponses[questionIndex] === index
                              && !response.correct}"
                                     :key="index">
                                  {{ index | charIndex }}. {{ response.text }}
                                </div>
                              </div>
                            </div>
                            <!--/questionContainer-->

                            <!--quizCompletedResult-->
                            <div v-if="chosenQuiz && questionIndex === quiz.questions.length"
                                 v-bind:key="questionIndex"
                                 class="quizCompleted has-text-centered">

                              <!-- quizCompletedIcon: Achievement Icon -->
                              <span class="icon">
                <i class="fa"
                   :class="score()>3
                   ?'fa-check-circle-o is-active':'fa-times-circle'">
                </i>
              </span>

                              <!--resultTitleBlock-->
                              <h2 class="title">
                                ¡Buen trabajo!
                              </h2>
                              <div class="progressContainer">

                                <div class="progress">
                                  <div class="progress-bar bg-success" role="progressbar"
                                       :style="{ width: (corrects/quiz.questions.length)*100+'%'}"
                                       aria-valuemin="0" aria-valuemax="100">{{corrects}}</div>
                                  <div class="progress-bar bg-danger" role="progressbar"
                                       :style="{ width: (incorrects/quiz.questions.length)*100+'%'}"
                                       aria-valuemin="0" aria-valuemax="100">{{incorrects}}</div>
                                </div>
                              </div>
                              <p class="subtitle">
                                Puntuación total: {{ score() }} / 10
                              </p>
                              <br>
                              <a class="button" @click="restart()">Volver a empezar
                                <i class="fa fa-refresh"></i>
                              </a>
                              <!--/resultTitleBlock-->

                            </div>
                            <!--/quizCompetedResult-->

                          </transition>

                        </div>
                        <!--/questionBox-->

                      </section>
                    </transition>
                    <!--/container-->
                  </div>
              </section>
            </div>
          </div>
        </section>
        <section v-if="chosenAsignatura && !chosenSection">
          <div class="profile profile-default">
            <div class="profile__image"><img src="https://www.wwno.org/sites/wwno/files/201409/5843577306_1a98149efb_o.jpg" alt="Doggo"/></div>
            <div class="profile__info">
              <h3>Exámenes y autoevaluaciones</h3>
              <p class="profile__info__extra">Practica con exámenes de años anteriores.</p>
              <p class="profile__info__extra">También puedes descargar un recopilatorio
                de exámenes de otras convocatorias.</p>
            </div>
            <div class="profile__cta">
              <a class="button"
                 @click="chooseSection('examenes'),
                 clearAllFilters(),
                 setFilter('primero', currentAsignatura.id)">
                Empezar</a></div>
          </div>
          <div class="profile profile-default">
            <div class="profile__image"><img src="https://previews.123rf.com/images/boarding1now/boarding1now1607/boarding1now160700019/61445985-group-of-people-holding-with-hands-the-word-info-information-message-news-announcement-announce.jpg" alt="Doggo"/></div>
            <div class="profile__info">
              <h3>Información importante</h3>
              <p class="profile__info__extra">Guía académica.</p>
              <p class="profile__info__extra">Horario del examen.</p>
              <p class="profile__info__extra">Sistema de evaluación.</p>
              <p class="profile__info__extra">Estadísticas de la asignatura.</p>
            </div>
            <div class="profile__cta">
              <a class="button" @click="chooseSection('info')">Ver información</a></div>
          </div>
          <div class="profile profile-default">
            <div class="profile__image"><img src="https://st.focusedcollection.com/13397678/i/1800/focused_168147658-stock-photo-university-lecturer-young-students-class.jpg" alt="Doggo"/></div>
            <div class="profile__info">
              <h3>Videoclases</h3>
              <p class="profile__info__extra">Tutorías grabadas de profesores universitarios.</p>
            </div>
            <div class="profile__cta"><a class="button">Ver videoclases</a></div>
          </div>
          <div class="profile profile-default">
            <div class="profile__image"><img src="https://i.pinimg.com/originals/71/af/26/71af260f19af61adc1bc408d72fe2778.jpg" alt="Apuntes"/></div>
            <div class="profile__info">
              <h3>Apuntes y material</h3>
              <p class="profile__info__extra">Descárgate los apuntes más utilizados para esta
                asignatura.</p>
            </div>
            <div class="profile__cta">
              <a class="button" @click="chooseSection('apuntes')">Ir a apuntes</a></div>
          </div>
        </section>

        <div v-if="chosenSection && chosenSection ==='apuntes'">
          <section
            v-for="pdf in currentAsignatura.apuntes"
            v-bind:key="pdf.id"
          >
            <div class="profile profile-long">
              <div class="profile__info">
                <h3>{{pdf.name}}</h3>
              </div>
              <div class="profile__cta" style="border: none; padding: 0;">
                <b-link
                  v-if="!pdf.wuolah"
                  target="_blank" class="button"
                  :href="'/pdfs/'+currentAsignatura.curso+
                  '/'+currentAsignatura.id+'/'+pdf.filename">
                  Descargar PDF</b-link>
                <b-link
                  v-if="pdf.wuolah"
                  target="_blank" class="button"
                  :href="pdf.link">
                   Abrir en Wuolah</b-link>
              </div>
            </div>
          </section>
        </div>

<!--        Información general-->
        <section v-if="chosenSection && chosenSection ==='info'">
          <div class="profile profile-long"
               style="grid-template-columns: none !important; padding: 20px 20px 15px;">
            <a class="button" v-b-toggle.collapse-1>Información general</a>
            <b-collapse id="collapse-1" class="mt-2">
              <div class="profile__stats">
                <p class="profile__stats__title">Curso</p>
                <h5 class="profile__stats__info">{{currentAsignatura.course_dg}}</h5>
              </div>
              <div class="profile__stats">
                <p class="profile__stats__title">Cuatrimestre</p>
                <h5>{{currentAsignatura.cuatrimestre}}</h5>
              </div>
              <div class="profile__stats">
                <p class="profile__stats__title">Créditos</p>
                <h5 class="profile__stats__info">{{currentAsignatura.credits}}</h5>
              </div>
              <div class="profile__cta">
                <b-link target="_blank" class="btn btn-success" :href="currentAsignatura.guiasrc">
                  Ir a la guía oficial</b-link>
                <!--                  <a class="button" target="_blank"-->
                <!--                     :href="currentAsignatura.guiasrc">Ir a la guía</a>-->
              </div>
            </b-collapse>
          </div>
        </section>

<!--        Sistema de evaluación-->
        <section v-if="chosenSection && chosenSection ==='info'">
          <div class="profile profile-long"
               style="grid-template-columns: none !important; padding: 20px 20px 15px;">
            <a class="button" v-b-toggle.collapse-2>Sistema de evaluación</a>
            <b-collapse id="collapse-2" class="mt-2">
              <div class="profile__stats">
                <p class="profile__stats__title">PEC?</p>
                <h5 class="profile__stats__info">
                  {{currentAsignatura.pec}} - {{currentAsignatura.pec_info}}</h5>
              </div>
              <div class="profile__stats">
                <p class="profile__stats__title">Nota final:</p>
                <h5>{{currentAsignatura.ponderacion}}</h5>
              </div>
            </b-collapse>
          </div>
        </section>

<!--        Botonera inferior-->

        <div class="profile profile-long"
             style="grid-template-columns: repeat(2,1fr) !important; padding: 20px 20px 15px;">
          <a class="btn" @click="chosenAsignatura=false, chosenSubject=false,
           chosenQuiz=false, chooseSection(null)">
            Elegir otra asignatura</a>
          <a class="btn" @click="chosenSubject=False,
          chooseSection(null)">
            Volver al menú</a>
        </div>
      </main>
    </div>
  </main>
  </div>
</template>
<script>
import _ from 'lodash';
import { ASIGNATURAS, ASIGNATURAS_META, EXAMS } from './config/config';

const numQuestions = 2;

export default {
  components: {
    icon: { template: '<svg><use :xlink:href="use"/></svg>', props: ['use'] },
  },

  data() {
    return {
      started: false,
      elegidoCurso: false,
      currentCurso: null,
      chosenSubject: false,
      chosenAsignatura: false,
      currentAsignatura: null,
      chosenSection: null,
      modal: false,
      companies: [],
      dropdown: { height: 0 },
      convocatoria: { min: 20, max: 0 },
      filters: {
        primero: {}, segundo: {}, tercero: {}, cuarto: {}, convocatoria: 0,
      },
      menus: {
        primero: false, segundo: false, tercero: false, cuarto: false, convocatoria: false,
      },
      cursos: {
        primero: {
          id: 'primer_curso',
          name: 'Primero',
          bg_color: '#8FCFD2',
        },
        segundo: {
          id: 'segundo_curso',
          name: 'Segundo',
          bg_color: '#8FCFD2',
        },
        tercero: {
          id: 'tercer_curso',
          name: 'Tercero',
          bg_color: '#8FCFD2',
        },
        cuarto: {
          id: 'cuarto_curso',
          name: 'Cuarto',
          bg_color: '#8FCFD2',
        },
      },
      asignaturas: [],
      chosenQuiz: false,
      subjectMinutes: 40,
      subjectQuestions: 25,
      corrects: 0,
      incorrects: 0,
      quiz: {
        user: 'Dave',
        questions: {},
      },
      display: 'big',
      questionIndex: 0,
      userResponses: Array(numQuestions).fill(null),
      rightWrong: Array(numQuestions).fill(null),
      isActive: false,
      result: '',
      show: false,
      time: 50 * 60, // in seconds
      timer: null,
      heroes: [
        {
          id: 0, name: 'Batman', power: 'Fist fighting', badass: 10,
        },
        {
          id: 1, name: 'Superman', power: 'Laser eyes', badass: 7,
        },
        {
          id: 2, name: 'Flash', power: 'Too fast', badass: 5,
        },
        {
          id: 3, name: 'Spiderman', power: 'Just a nice guy', badass: 1,
        },
        {
          id: 4, name: 'Hulk', power: 'SMASH!', badass: 42,
        },
      ],
    };
  },
  filters: {
    charIndex(i) {
      return String.fromCharCode(97 + i);
    },
  },
  computed: {
    activeMenu() {
      return Object.keys(this.menus).reduce(($$, set, i) => ((this.menus[set]) ? i : $$), -1);
    },
    // eslint-disable-next-line vue/return-in-computed-property
    activeAsignaturas() {
      // eslint-disable-next-line func-names
      return Object.values(this.asignaturas).filter(
        (asignatura) => asignatura.curso === this.currentCurso,
      );
    },
    list() {
      const {
        cuarto, tercero, segundo, primero,
      } = this.activeFilters;

      const c = this.companies.filter(({
        subject, rating,
      }) => {
        if (rating < this.filters.convocatoria) return false;
        // eslint-disable-next-line no-bitwise
        if (cuarto.length && !~cuarto.indexOf(subject)) return false;
        // eslint-disable-next-line no-bitwise
        if (tercero.length && !~tercero.indexOf(subject)) return false;
        // eslint-disable-next-line no-bitwise
        if (segundo.length && !~segundo.indexOf(subject)) return false;
        // eslint-disable-next-line no-bitwise
        if (primero.length && !~primero.indexOf(subject)) return false;
        // eslint-disable-next-line no-bitwise
        // return !categories.length || categories.every((cat) => ~keywords.indexOf(cat));´
        return true;
      });
      // eslint-disable-next-line no-undef
      return _.orderBy(c, '-year');
    },
    temaslist() {
      const c = this.list.filter(({
        autoevaluacion,
      }) => autoevaluacion);
      return c;
    },
    exameneslist() {
      const c = this.list.filter(({
        autoevaluacion,
      }) => !autoevaluacion);
      return c;
    },
    quizOptions() {
      const q = {
        easy: {
          id: 'easy',
          title: '15 preguntas',
          subjectQuestions: 15,
        },
        standard: {
          id: '30preguntas',
          title: '30 preguntas',
          subjectQuestions: 30,
        },
        all: {
          id: 'all',
          title: 'Todas',
          subjectQuestions: this.subjectQuestions,
        },
      };
      return Object.values(q).filter(({
        subjectQuestions, id,
      }) => subjectQuestions < this.subjectQuestions || id === 'all');
    },

    activeFilters() {
      const {
        cuarto, tercero, segundo, primero,
      } = this.filters;

      return {
        cuarto: Object.keys(cuarto).filter((c) => cuarto[c]),
        tercero: Object.keys(tercero).filter((c) => tercero[c]),
        segundo: Object.keys(segundo).filter((c) => segundo[c]),
        // categories: Object.keys(categories).filter((c) => categories[c]),
        primero: Object.keys(primero).filter((c) => primero[c]),
        convocatoria: (this.filters.convocatoria > this.convocatoria.min)
          ? [this.filters.convocatoria]
          : [],
      };
    },
    timeLeft() {
      return `${this.minutes}:${this.seconds}`;
    },
    minutes() {
      return String(Math.floor(this.time / 60)).padStart(2, '0');
    },
    seconds() {
      return String(this.time % 60).padStart(2, '0');
    },

    filteredHeroes() {
      return this.heroes;
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
    chooseSection(section) {
      window.scrollTo(0, 0);
      this.chosenSection = section;
      this.chosenQuiz = false;
    },
    chooseCurso(curso) {
      this.started = true;
      this.currentCurso = curso.id;
      this.asignaturas = ASIGNATURAS_META;
    },
    chooseAsignatura(asignatura) {
      this.chosenAsignatura = true;
      this.currentAsignatura = asignatura;
    },
    beautifyOption(option) {
      return option.charAt(0).toUpperCase() + option.replace(/_/g, ' ').slice(1);
    },
    onResize() {
      if (window.innerWidth > 760) {
        this.display = 'big';
      } else {
        this.display = 'smol';
      }
    },
    getDisplay(menu) {
      this.onResize();
      if (menu === 'convocatoria') return 'Año';
      if (menu === 'cuarto') {
        if (this.display === 'big') return 'Cuarto';
        return '4º';
      } if (menu === 'tercero') {
        if (this.display === 'big') return 'Tercero';
        return '3º';
      } if (menu === 'segundo') {
        if (this.display === 'big') return 'Segundo';
        return '2º';
      }
      if (this.display === 'big') return 'Primero';
      return '1º';
    },
    setFilter(filter, option) {
      if (filter === 'cuarto') {
        if (!this.filters[filter][option]) {
          Object.keys(this.filters.primero).forEach((f) => {
            this.filters.primero[f] = false;
          });
          Object.keys(this.filters.segundo).forEach((f) => {
            this.filters.segundo[f] = false;
          });
          Object.keys(this.filters.tercero).forEach((f) => {
            this.filters.tercero[f] = false;
          });
        }
        this.filters[filter][option] = !this.filters[filter][option];
      } else if (filter === 'tercero') {
        if (!this.filters[filter][option]) {
          Object.keys(this.filters.primero).forEach((f) => {
            this.filters.primero[f] = false;
          });
          Object.keys(this.filters.segundo).forEach((f) => {
            this.filters.segundo[f] = false;
          });
          Object.keys(this.filters.cuarto).forEach((f) => {
            this.filters.cuarto[f] = false;
          });
        }
        this.filters[filter][option] = !this.filters[filter][option];
      } else if (filter === 'segundo') {
        if (!this.filters[filter][option]) {
          Object.keys(this.filters.primero).forEach((f) => {
            this.filters.primero[f] = false;
          });
          Object.keys(this.filters.tercero).forEach((f) => {
            this.filters.tercero[f] = false;
          });
          Object.keys(this.filters.cuarto).forEach((f) => {
            this.filters.cuarto[f] = false;
          });
        }
        this.filters[filter][option] = !this.filters[filter][option];
      } else if (filter === 'primero') {
        if (!this.filters[filter][option]) {
          Object.keys(this.filters.segundo).forEach((f) => {
            this.filters.segundo[f] = false;
          });
          Object.keys(this.filters.tercero).forEach((f) => {
            this.filters.tercero[f] = false;
          });
          Object.keys(this.filters.cuarto).forEach((f) => {
            this.filters.cuarto[f] = false;
          });
        }
        this.filters[filter][option] = !this.filters[filter][option];
      } else {
        setTimeout(() => {
          this.clearFilter(filter, option, this.filters[filter][option]);
        }, 100);
      }
    },

    clearFilter(filter, except, active) {
      if (filter === 'convocatoria') {
        this.filters[filter] = this.convocatoria.min;
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

    restart() {
      // this.clearAllFilters();
      this.questionIndex = 0;
      this.corrects = 0;
      this.incorrects = 0;
      this.userResponses = Array(this.quiz.questions.length).fill(null);
      this.time = 50 * 60;
      this.chosenQuiz = false;
      this.chosenSubject = false;
    },
    chooseSubject(name, subject) {
      this.title = subject.name;
      this.examDate = subject.slogan;
      this.numQuestions = subject.questions;
      // const exams = this[subject].examNames[0].concat(this[subject].examNames[1]);
      const exams = EXAMS[name][subject.year][subject.month];
      this.quiz.questions = exams
        .sort(() => Math.random() - 0.5)
        .slice(0, subject.questions);
      this.userResponses = Array(subject.questions).fill(null);
      this.rightWrong = Array(subject.questions).fill(null);
      this.time = subject.minutes * 60;
      this.subjectMinutes = subject.minutes;
      this.subjectQuestions = subject.questions;
      this.corrects = 0;
      this.incorrects = 0;
      this.plusScore = subject.plusScore;
      this.minusScore = subject.minusScore;
      this.chosenSubject = true;
    },
    chooseOptions(option) {
      this.subjectMinutes = option.subjectMinutes;
      this.quiz.questions = this.quiz.questions
        .slice(0, option.subjectQuestions);
      this.userResponses = Array(option.subjectQuestions).fill(null);
      this.rightWrong = Array(option.subjectQuestions).fill(null);
      // this.time = 3600;
      this.chosenQuiz = true;
    },
    selectOption(index, response) {
      // TODO: fix changing wrong answer to wrong answer
      this.rightWrong[this.questionIndex] = response.correct === true;
      this.corrects = this.rightWrong.reduce((n, val) => n + (val === true), 0);
      this.incorrects = this.rightWrong.reduce((n, val) => n + (val === false), 0);
      // eslint-disable-next-line no-undef
      Vue.set(this.userResponses, this.questionIndex, index);
    },
    next() {
      if (this.questionIndex < this.quiz.questions.length) {
        this.questionIndex += 1;
      }
    },

    prev() {
      if (this.questionIndex > 0) {
        this.questionIndex -= 1;
      }
    },
    // Return "true" count in rightWrong
    score() {
      let score = this.rightWrong.filter((v) => v).length * this.plusScore;
      score -= this.rightWrong.filter((v) => v === false).length * this.minusScore;
      return Math.max(Math.round(score * 100) / 100, 0);
    },
    decrementOrAlert() {
      if (this.time > 0) {
        // eslint-disable-next-line no-plusplus
        this.time--;
        return;
      }
      // alert('Se acabó el tiempo!');
      clearInterval(this.timer);
    },
  },

  created() {
    this.timer = setInterval(this.decrementOrAlert, 1000);
    window.addEventListener('resize', this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
  },
  beforeMount() {
    this.companies = ASIGNATURAS;
    this.companies = this.companies.filter((company) => company.verified);

    this.companies.forEach(({ rating, subject, course }) => {
      if (course === 'Cuarto') {
        this.$set(this.filters.cuarto, subject, false);
      } else if (course === 'Tercero') {
        this.$set(this.filters.tercero, subject, false);
      } else if (course === 'Segundo') {
        this.$set(this.filters.segundo, subject, false);
      } else if (course === 'Primero') {
        this.$set(this.filters.primero, subject, false);
      }
      if (this.convocatoria.max < rating) this.convocatoria.max = rating;
      if (this.convocatoria.min > rating) {
        this.convocatoria.min = rating;
        this.filters.convocatoria = rating;
      }

      /*      keywords.forEach((category) => {
        this.$set(this.filters.categories, category, false);
      }); */
    });
  },
};

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
<style scoped src="@/assets/css/styles.css">
</style>
