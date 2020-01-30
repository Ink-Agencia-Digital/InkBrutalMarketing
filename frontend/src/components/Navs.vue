<template>
  <div class="wrapper" id="navbarSupportedContent">
    <div class="sidebar-wrapper">
      <div class="user-info">
        <div class="image">
          <img src="@/assets/logo.png" alt="Perfil" width="48" height="48" />
        </div>
      </div>
      <div class="menu">
        <div
          class="slimScrollDiv"
          style="position: relative; width: auto; height: 163px;"
        >
          <ul class="sidebar-nav list">
            <li class="header">Menu de navegación</li>
            <li>
              <router-link
                :to="{ name: 'inicio' }"
                class="waves-effect waves-block"
              >
                Inicio</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'listar_persona' }"
                class="waves-effect waves-block"
              >
                Persona</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'listar_empresa' }"
                class="waves-effect waves-block"
              >
                Empresa</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'listar_proyecto' }"
                class="waves-effect waves-block"
              >
                Proyecto</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'listar_medio' }"
                class="waves-effect waves-block"
              >
                Medio</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'listar_proceso' }"
                class="waves-effect waves-block"
              >
                Proceso</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'lista_contenido' }"
                class="waves-effect waves-block"
              >
                Lista de contenido</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'planificacion_emails' }"
                class="waves-effect waves-block"
              >
                Planificación</router-link
              >
            </li>
            <li>
              <router-link
                :to="{ name: 'calendario' }"
                class="waves-effect waves-block"
              >
                Calendario</router-link
              >
            </li>
            <li>
              <a href="/accounts/logout/" class="waves-effect waves-block"
                >Salir</a
              >
            </li>
          </ul>
        </div>
      </div>
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
