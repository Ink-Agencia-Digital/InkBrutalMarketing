import Vue from "vue";
import VueRouter from "vue-router";
import Inicio from "@/views/Inicio";
import Empresa from "@/views/Empresa";
import PrincipalEmpresa from "@/views/PrincipalEmpresa";
import Comportamiento from "@/views/Comportamiento";
import Objetivo from "@/views/Objetivo";
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
    path: "/comportamiento",
    name: "comportamiento",
    component: Comportamiento
  },
  {
    path: "/objetivo",
    name: "objetivo",
    component: Objetivo
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
