import ANALISIS from './analisis-datos-meta.json';
import APRENDIZAJE from './aprendizaje.json';
import ATENCION from './atencion.json';
import EMOCION from './emocion.json';
import FUNDAMENTOS from './fundamentos-investigacion.json';
import HISTORIA from './historia.json';
import MOTIVACION from './motivacion.json';
import PSICOBIOLOGIA from './psicobiologia.json';
import SOCIAL from './psicologia-social.json';

// eslint-disable-next-line import/prefer-default-export
export const ASIGNATURAS_PRIMERO = Object.freeze(ANALISIS.concat(
  APRENDIZAJE, ATENCION, EMOCION, FUNDAMENTOS, SOCIAL, HISTORIA, MOTIVACION, PSICOBIOLOGIA,
));
