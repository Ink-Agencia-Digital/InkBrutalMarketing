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
    path: "/principalEmpresa",
    name: "PrincipalEmpresa",
    component: PrincipalEmpresa
  },
  {
    path: "/empresa",
    name: "Empresa",
    component: Empresa
  },
  {
    path: "/comportamiento",
    name: "Comportamiento",
    component: Comportamiento
  },
  {
    path: "/objetivo",
    name: "Objetivo",
    component: Objetivo
  },
  {
    path: "/proceso",
    name: "Proceso",
    component: Proceso
  },
  {
    path: "/lista",
    name: "Lista",
    component: Lista
  },
  {
    path: "/planificacion",
    name: "Planificacion",
    component: Planificacion
  },
  {
    path: "/calendario",
    name: "Calendario",
    component: Calendario
  }
];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes
});

export default router;
