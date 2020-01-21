<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark my-navbar"
    style="background-color: #344675;"
  >
    <router-link :to="{ name: 'inicio' }" class="navbar-brand">
      InkBrutalMarketing</router-link
    >
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <router-link :to="{ name: 'inicio' }" class="nav-link">
            Inicio</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'listar_empresa' }" class="nav-link">
            Persona</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'listar_proyecto' }" class="nav-link">
            Proyecto</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'comportamiento' }" class="nav-link">
            Comportamientos</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'objetivo' }" class="nav-link">
            Objetivos</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'proceso' }" class="nav-link">
            Proceso</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'lista' }" class="nav-link">
            Lista de contenido</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'planificacion' }" class="nav-link">
            Planificación</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'calendario' }" class="nav-link">
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
  name: "NavsComponent"
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
.my-navbar {
  border-bottom: 1px solid #ddd;
}
</style>
