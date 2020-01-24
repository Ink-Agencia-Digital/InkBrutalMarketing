<template>
  <div class="wrapper" id="navbarSupportedContent">
    <div class="sidebar-wrapper">
      <ul class="sidebar-nav">
        <li class="sidebar-brand">
          <router-link :to="{ name: 'inicio' }" class="navbar-brand">
            InkBrutalMarketing</router-link
          >
        </li>
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
          <router-link :to="{ name: 'PrincipalMedio' }" class="nav-link">
            Medio</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'listar_comportamiento' }" class="nav-link">
            Comportamientos</router-link
          >
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'listar_objetivo' }" class="nav-link">
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
    <div class="">
      <header class="header navbar-light bg-faded">
        <div class="container-fluid">
          <div class="row text-center">
            <button
              type="button"
              name="button"
              class="btn hamburguer-btn"
              id="menu"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <span class="page-title">MarketMail</span>
            <div class="profile-pic"></div>
          </div>
        </div>
      </header>
    </div>
  </div>
</template>
<script>
export default {
  name: "NavsComponent"
};
</script>

<style></style>
