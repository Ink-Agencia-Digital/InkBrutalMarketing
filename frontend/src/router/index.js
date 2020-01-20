import Vue from "vue";
import VueRouter from "vue-router";
import Inicio from "@/views/Inicio";
import Empresa from "@/views/Empresa";
import PrincipalEmpresa from "@/views/PrincipalEmpresa";
import Persona from "@/views/Persona";
import Proyecto from "@/views/Proyecto";
import PrincipalProyecto from "@/views/PrincipalProyecto";
import PrincipalMedio from "@/views/PrincipalMedio";
import Medio from "@/views/Medio";
import PrincipalComportamiento from "@/views/PrincipalComportamiento";
import Comportamiento from "@/views/Comportamiento";
import PrincipalObjetivo from "@/views/PrincipalObjetivo";
import Objetivo from "@/views/Objetivo";
import PrincipalProceso from "@/views/PrincipalProceso";
import Proceso from "@/views/Proceso";
import Lista from "@/views/Lista";
import Planificacion from "@/views/Planificacion";
import Calendario from "@/views/Calendario";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "inicio",
    component: Inicio
  },
  {
    path: "/principal-empresa",
    name: "principal_empresa",
    component: PrincipalEmpresa
  },
  {
    path: "/empresa",
    name: "empresa",
    component: Empresa
  },
  {
    path: "/persona",
    name: "persona",
    component: Persona
  },
  {
    path: "/principal-proyecto",
    name: "principal_proyecto",
    component: PrincipalProyecto
  },
  {
    path: "/proyecto",
    name: "proyecto",
    component: Proyecto
  },
  {
    path: "/principal-medio",
    name: "principal_medio",
    component: PrincipalMedio
  },
  {
    path: "/medio",
    name: "medio",
    component: Medio
  },
  {
    path: "/principal-comportamiento",
    name: "principal_comportamiento",
    component: PrincipalComportamiento
  },
  {
    path: "/comportamiento",
    name: "comportamiento",
    component: Comportamiento
  },
  {
    path: "/principal-objetivo",
    name: "principal_objetivo",
    component: PrincipalObjetivo
  },
  {
    path: "/objetivo",
    name: "objetivo",
    component: Objetivo
  },
  {
    path: "/principal-proceso",
    name: "principal_proceso",
    component: PrincipalProceso
  },
  {
    path: "/proceso",
    name: "proceso",
    component: Proceso
  },
  {
    path: "/lista",
    name: "lista",
    component: Lista
  },
  {
    path: "/planificacion",
    name: "planificacion",
    component: Planificacion
  },
  {
    path: "/calendario",
    name: "calendario",
    component: Calendario
  }
];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes
});

export default router;
