import DESARROLLOI from './desarrollo-i.json';
import DIFERENCIAS_INDIVIDUALES from './diferencias-individuales.json';
import DISENOS_INVESTIGACION from './disenos-investigacion.json';
import FISIOLOGICA from './psicologia-fisiologica.json';
import MEMORIA from './memoria.json';
import PENSAMIENTO from './pensamiento.json';
import PERCEPCION from './percepcion.json';
import PSICOMETRIA from './psicometria.json';
import PSICOPATOLOGIA from './psicopatologia.json';

// eslint-disable-next-line import/prefer-default-export
export const ASIGNATURAS_SEGUNDO = Object.freeze(DESARROLLOI.concat(
  DIFERENCIAS_INDIVIDUALES, DISENOS_INVESTIGACION, FISIOLOGICA, MEMORIA,
  PENSAMIENTO, PERCEPCION, PSICOMETRIA, PSICOPATOLOGIA,
));
