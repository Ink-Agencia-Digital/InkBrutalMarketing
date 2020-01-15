<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark alt"
    style="background-color: #344675;"
  >
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link :to="{ name: 'inicio' }" class="nav-link">
            Inicio</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'PrincipalEmpresa' }" class="nav-link">
            Persona</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Comportamiento' }" class="nav-link">
            Comportamientos</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Objetivo' }" class="nav-link">
            Objetivos</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Proceso' }" class="nav-link">
            Proceso</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Lista' }" class="nav-link">
            Lista de contenido</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Planificacion' }" class="nav-link">
            Planificación</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'Calendario' }" class="nav-link">
            Calendario</router-link
          >
        </li>
        <li class="nav-item">
          <a href="/accounts/logout/" class="nav-link">Salir</a>
        </li>
      </ul>
    </div>
  </nav>
</template>
<script>
export default {
  name: "Navs"
};
</script>
<style>
.alt {
  padding: 1%;
  padding-left: 30%;
}
.alt1 {
  padding: 1%;
  padding-left: 2%;
}
</style>
