import Vue from "vue";
import VueRouter from "vue-router";
import Inicio from "@/views/Inicio";

import ListarEmpresa from "@/views/Empresa/Listar";
import CrearEmpresa from "@/views/Empresa/Crear";
import EditarEmpresa from "@/views/Empresa/Editar";

import CrearPersona from "@/views/Persona/Crear";
import EditarPersona from "@/views/Persona/Editar";

import ListarProyecto from "@/views/Proyecto/Listar";
import CrearProyecto from "@/views/Proyecto/Crear";
import EditarProyecto from "@/views/Proyecto/Editar";

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
    path: "/listar-empresa",
    name: "listar_empresa",
    component: ListarEmpresa
  },
  {
    path: "/crear-empresa",
    name: "crear_empresa",
    component: CrearEmpresa
  },
  {
    path: "/editar-empresa/:id",
    name: "editar_empresa",
    component: EditarEmpresa,
    props: true
  },
  {
    path: "/crear-persona",
    name: "crear_persona",
    component: CrearPersona
  },
  {
    path: "/editar-persona/:id",
    name: "editar_persona",
    component: EditarPersona,
    props: true
  },
  {
    path: "/listar-proyecto",
    name: "listar_proyecto",
    component: ListarProyecto
  },
  {
    path: "/crear-proyecto",
    name: "crear_proyecto",
    component: CrearProyecto
  },
  {
    path: "/editar-proyecto/:id",
    name: "editar_proyecto",
    component: EditarProyecto,
    props: true
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
