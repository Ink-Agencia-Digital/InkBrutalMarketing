<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Editar Medio</h2>
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
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="medio">Nombre del Medio</label>
                <input
                  type="text"
                  class="form-control"
                  id="medio"
                  v-model="MDO_Nombre_Medio"
                />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="icono">
                  Icono del Medio
                  <i
                    id="mostrar-icono"
                    class="form-label fa "
                    v-bind:class="this.MDO_Icono_Medio"
                  ></i>
                </label>
                <input
                  type="text"
                  class="form-control"
                  id="icono"
                  v-model="MDO_Icono_Medio"
                  v-on:keyup="icon"
                />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="descripcion">Descripción</label>
                <textarea
                  class="form-control"
                  aria-label="With textarea"
                  v-model="MDO_Descripcion_Medio"
                ></textarea>
              </div>
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
  props: {
    id: {
      type: Number,
      required: true
    },
    nombreAnterior: {
      type: String,
      required: true
    },
    descripcionAnterior: {
      type: String,
      required: true
    },
    iconoAnterior: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      MDO_Nombre_Medio: this.nombreAnterior,
      MDO_Descripcion_Medio: this.descripcionAnterior,
      MDO_Icono_Medio: this.iconoAnterior,
      error: null
    };
  },
  methods: {
    icon: function() {
      var contenido = "";
      for (var i = 0; i < this.MDO_Icono_Medio.length; i++) {
        if (this.MDO_Icono_Medio.charAt(i) == " ") contenido = contenido + "-";
        else contenido = contenido + this.MDO_Icono_Medio.charAt(i);
      }
      this.MDO_Icono_Medio = contenido;
    },
    onSubmit() {
      if (!this.MDO_Nombre_Medio) {
        this.error = "Por favor digite un nombre de medio";
      } else if (!this.MDO_Descripcion_Medio) {
        this.error = "Por favor digite una descripción del medio";
      } else if (!this.MDO_Icono_Medio) {
        this.error = "Por favor digite una icono para el medio";
      } else if (this.MDO_Nombre_Medio.length > 150) {
        this.error =
          "El nombre del medio no puede ser superior a 150 caracteres";
      } else if (this.MDO_Descripcion_Medio.length > 1000) {
        this.error =
          "La descripción del medio no puede ser superior a 1000 caracteres";
      } else if (this.MDO_Icono_Medio.length > 1000) {
        this.error =
          "El Icono del medio no puede ser superior a 1000 caracteres";
      } else {
        let endpoint = `/api/medio/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, {
          MDO_Nombre_Medio: this.MDO_Nombre_Medio,
          MDO_Descripcion_Medio: this.MDO_Descripcion_Medio,
          MDO_Icono_Medio: this.MDO_Icono_Medio
        }).then(() => {
          this.$router.push({
            name: "listar_medio"
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/medio/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.nombreAnterior = data.MDO_Nombre_Medio;
    to.params.descripcionAnterior = data.MDO_Descripcion_Medio;
    to.params.iconoAnterior = data.MDO_Icono_Medio;
    return next();
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
