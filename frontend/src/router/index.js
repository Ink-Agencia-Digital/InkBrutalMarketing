import Vue from "vue";
import VueRouter from "vue-router";
import Inicio from "@/views/Inicio";

import ListarEmpresa from "@/views/Empresa/Listar";
import CrearEmpresa from "@/views/Empresa/Crear";
import EditarEmpresa from "@/views/Empresa/Editar";

import ListarPersona from "@/views/Persona/Listar";
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

import ListarProceso from "@/views/Proceso/Listar";
import CrearProceso from "@/views/Proceso/Crear";
import EditarProceso from "@/views/Proceso/Editar";

import ListaContenido from "@/views/Contenido/Lista";

import PlanificacionEmail from "@/views/Planificacion/Planificacion";

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
    path: "/listar-persona",
    name: "listar_persona",
    component: ListarPersona
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
    path: "/listar-comportamiento/:id",
    name: "listar_comportamiento",
    component: ListarComportamiento,
    props: true
  },
  {
    path: "/crear-comportamiento/:id",
    name: "crear_comportamiento",
    component: CrearComportamiento,
    props: true
  },
  {
    path: "/editar-comportamiento",
    name: "editar_comportamiento",
    component: EditarComportamiento
  },
  {
    path: "/listar-objetivo/:id",
    name: "listar_objetivo",
    component: ListarObjetivo,
    props: true
  },
  {
    path: "/crear-objetivo/:id",
    name: "crear_objetivo",
    component: CrearObjetivo,
    props: true
  },
  {
    path: "/editar-objetivo/:id",
    name: "editar_objetivo",
    component: EditarObjetivo,
    props: true
  },
  {
    path: "/listar-proceso",
    name: "listar_proceso",
    component: ListarProceso
  },
  {
    path: "/crear-proceso",
    name: "crear_proceso",
    component: CrearProceso
  },
  {
    path: "/editar-proceso",
    name: "editar_proceso",
    component: EditarProceso,
    props: true
  },
  {
    path: "/lista-contenido",
    name: "lista_contenido",
    component: ListaContenido
  },
  {
    path: "/planificacion-emails",
    name: "planificacion_emails",
    component: PlanificacionEmail
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
