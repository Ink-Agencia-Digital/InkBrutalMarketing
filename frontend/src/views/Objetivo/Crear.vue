<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Crear Objetivos y desafíos</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'listar_objetivo' }"
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
              <h3>Persona</h3>
              <select
                id="persona"
                class="form-control"
                required
                v-model="OBJ_Persona_Objetivo"
                disabled
              >
                <option selected disabled value="">
                  --Seleccione una persona--
                </option>
                <option
                  v-for="psn in personas"
                  :key="psn.PSN_Id_Persona"
                  :value="psn.PSN_Id_Persona"
                >
                  {{ psn.PSN_Nombres_Persona }} {{ psn.PSN_Apellidos_Persona }}
                </option>
              </select>
            </div>
            <br />
            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">
                      #
                    </th>
                    <th scope="col">
                      Pregunta
                    </th>
                    <th scope="col">
                      Respuesta
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="prg in preguntas" :key="prg.PRG_Id_Pregunta">
                    <th scope="row">
                      {{ prg.PRG_Id_Pregunta }}
                    </th>
                    <td>
                      <label class="">
                        {{ prg.PRG_Nombre_Pregunta }}
                      </label>
                    </td>
                    <td>
                      <input
                        type="text"
                        class="form-control"
                        :id="'prg' + prg.PRG_Id_Pregunta"
                        placeholder="Respuesta"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
              <div class="my-4">
                <p v-show="loadingPreguntas">...Cargando...</p>
                <button
                  v-show="nextPregunta"
                  @click="getPreguntas('MAS')"
                  class="btn btn-sm btn-outline-success"
                >
                  Cargar Más
                </button>
              </div>
            </div>
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
            <router-link
              :to="{ name: 'listar_objetivo' }"
              class="btn btn-danger"
            >
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
    }
  },
  data() {
    return {
      OBJ_Persona_Objetivo: this.id,
      personas: [],
      preguntas: [],
      nextPregunta: null,
      loadingPreguntas: false,
      error: null
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    getPreguntas() {
      let endpoint = `/api/pregunta/${this.id}/filtro/`;
      apiService(endpoint).then(data => {
        this.preguntas.push(...data.results);
      });
    },
    onSubmit() {
      if (!this.OBJ_Persona_Objetivo) {
        this.error = "Por favor seleccione una persona";
      }
      this.preguntas.forEach(prg => {
        var miCampoTexto = document.getElementById("prg" + prg.PRG_Id_Pregunta)
          .value;
        if (miCampoTexto.length == 0) {
          this.error =
            "Por favor digite la respuesta de la pregunta " +
            prg.PRG_Id_Pregunta;
        } else {
          let endpoint = "/api/objetivo/";
          let method = "POST";
          apiService(endpoint, method, {
            OBJ_Persona_Objetivo: this.OBJ_Persona_Objetivo,
            OBJ_Pregunta_Objetivo: prg.PRG_Id_Pregunta,
            OBJ_Respuesta_Objetivo: miCampoTexto
          });
        }
      });
      this.$router.push({ name: "listar_objetivo" });
    }
  },
  created() {
    this.getPersonas();
    this.getPreguntas();
  }
};
</script>
