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

import ListarMedio from "@/views/Medio/Listar";
import CrearMedio from "@/views/Medio/Crear";
import EditarMedio from "@/views/Medio/Editar";

import ListarComportamiento from "@/views/Comportamiento/Listar";
import CrearComportamiento from "@/views/Comportamiento/Crear";
import EditarComportamiento from "@/views/Comportamiento/Editar";

import ListarObjetivo from "@/views/Objetivo/Listar";
import CrearObjetivo from "@/views/Objetivo/Crear";
import EditarObjetivo from "@/views/Objetivo/Editar";

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
    path: "/listar-medio",
    name: "listar_medio",
    component: ListarMedio
  },
  {
    path: "/crear-medio",
    name: "crear_medio",
    component: CrearMedio
  },
  {
    path: "/editar-medio/:id",
    name: "editar_medio",
    component: EditarMedio,
    props: true
  },
  {
    path: "/listar-comportamiento",
    name: "listar_comportamiento",
    component: ListarComportamiento
  },
  {
    path: "/crear-comportamiento",
    name: "crear_comportamiento",
    component: CrearComportamiento
  },
  {
    path: "/editar-comportamiento",
    name: "editar_comportamiento",
    component: EditarComportamiento
  },
  {
    path: "/listar-objetivo",
    name: "listar_objetivo",
    component: ListarObjetivo
  },
  {
    path: "/crear-objetivo",
    name: "crear_objetivo",
    component: CrearObjetivo
  },
  {
    path: "/editar-objetivo/:id",
    name: "editar_objetivo",
    component: EditarObjetivo
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
