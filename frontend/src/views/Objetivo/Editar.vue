<template>
  <div class="container">
    <div class="col-md-8">
      <form @submit.prevent="onSubmit">
        <br /><br />
        <h1>Objetivos y desafíos</h1>
        <br />
        <div class="form-group">
          <h3>Persona</h3>
          <select
            id="persona"
            class="form-control"
            required
            v-model="OBJ_Persona_Objetivo"
          >
            <option selected value="">--Seleccione una persona--</option>
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
        <label>{{ OBJ_Pregunta_Objetivo }}</label>
        <label></label>
        <input
          type="text"
          class="form-control"
          :v-model="OBJ_Respuesta_Objetivo"
          placeholder="Respuesta"
        />
        <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
        <br />
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
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  props: {
    id: {
      type: Number,
      required: true
    },
    personaAnterior: {
      type: String,
      required: true
    },
    preguntaAnterior: {
      type: String,
      required: true
    },
    respuestaAnterior: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      personas: [],
      OBJ_Persona_Objetivo: this.personaAnterior,
      OBJ_Pregunta_Objetivo: this.preguntaAnterior,
      OBJ_Respuesta_Objetivo: this.respuestaAnterior,
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
    onSubmit() {
      if (!this.OBJ_Respuesta_Objetivo) {
        this.error = "Por favor digite los nombres";
      } else if (this.OBJ_Respuesta_Objetivo.length > 150) {
        this.error = "El cargo no puede ser superior a 45 caracteres";
      } else {
        let endpoint = `/api/objetivo/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, {
          OBJ_Persona_Objetivo: this.OBJ_Persona_Objetivo,
          OBJ_Pregunta_Objetivo: this.OBJ_Pregunta_Objetivo,
          OBJ_Respuesta_Objetivo: this.OBJ_Respuesta_Objetivo
        }).then(() => {
          this.$router.push({
            name: "listar_objetivo"
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/objetivo-join/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.personaAnterior = data.OBJ_Persona_Objetivo;
    to.params.preguntaAnterior = data.OBJ_Pregunta_Objetivo;
    to.params.respuestaAnterior = data.OBJ_Respuesta_Objetivo;
    return next();
  },
  created() {
    this.getPersonas();
  }
};
</script>
