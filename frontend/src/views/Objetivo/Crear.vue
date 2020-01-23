<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Objetivos y desafíos</h1>
        <br />
        <div class="form-group">
          <h3>Persona</h3>
          <select id="persona" class="form-control" required>
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
  data() {
    return {
      personas: [],
      preguntas: []
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
      let endpoint = "/api/pregunta/";
      apiService(endpoint).then(data => {
        this.preguntas.push(...data.results);
      });
    }
  },
  created() {
    this.getPersonas();
    this.getPreguntas();
  }
};
</script>
