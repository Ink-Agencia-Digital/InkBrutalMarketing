<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Crear Medio</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'listar_medio' }"
                class="btn btn-danger"
              >
                <i class="material-icons" style="font-size: 20px;">
                  keyboard_backspace
                </i>
                Volver
              </router-link>
            </li>
          </ul>
        </div>
        <div class="body">
          <form @submit.prevent="onSubmit">
            <div class="form-group">
              <h5 for="medio">Nombre del Medio</h5>
              <input
                type="text"
                class="form-control"
                id="medio"
                v-model="MDO_Nombre_Medio"
              />
            </div>
            <div class="form-group ">
              <h5 for="descripcion">Descripción</h5>
              <textarea
                class="form-control"
                aria-label="With textarea"
                v-model="MDO_Descripcion_Medio"
              ></textarea>
            </div>
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
            <router-link :to="{ name: 'listar_medio' }" class="btn btn-danger">
              Cancelar
            </router-link>
            &nbsp;
            <button
              type="submit"
              class="btn btn-dark"
              style="background-color: #344675;"
            >
              Guardar
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.MDO_Nombre_Medio) {
        this.error = "Por favor digite un nombre de medio";
      } else if (!this.MDO_Descripcion_Medio) {
        this.error = "Por favor digite una descripción del medio";
      } else if (this.MDO_Nombre_Medio.length > 150) {
        this.error =
          "El nombre del medio no puede ser superior a 150 caracteres";
      } else if (this.MDO_Descripcion_Medio.length > 1000) {
        this.error =
          "La descripción del medio no puede ser superior a 1000 caracteres";
      } else {
        let endpoint = "/api/medio/";
        let method = "POST";
        apiService(endpoint, method, {
          MDO_Nombre_Medio: this.MDO_Nombre_Medio,
          MDO_Descripcion_Medio: this.MDO_Descripcion_Medio
        }).then(() => {
          this.$router.push({
            name: "listar_medio"
          });
        });
      }
    }
  }
};
</script>

<style>
.background {
  position: absolute;
  z-index: 1;
  width: 98%;
  height: 169%;
  padding-top: 0%;
  padding-left: 0%;
  padding-right: 0%;
}
</style>
