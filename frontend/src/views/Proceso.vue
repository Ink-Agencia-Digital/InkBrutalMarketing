<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Proceso de Compra</h1>
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
                Etapa
              </th>
              <th scope="col">
                Idea
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="etp in etapas" :key="etp.ETP_Id_Etapa">
              <th scope="row">
                {{ etp.ETP_Id_Etapa }}
              </th>
              <td>
                <label class="" for="etapa1">
                  {{ etp.ETP_Descripcion_Etapa }}
                </label>
              </td>
              <td>
                <select id="idea" class="form-control" required>
                  <option selected value="">--Seleccione una Idea--</option>
                  <option
                    v-for="ida in ideas"
                    :key="ida.IDA_Id_Idea"
                    :value="ida.IDA_Id_Idea"
                  >
                    {{ ida.IDA_Descripcion_Idea }}
                  </option>
                </select>
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
      etapas: [],
      ideas: []
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    getEtapas() {
      let endpoint = "/api/etapa/";
      apiService(endpoint).then(data => {
        this.etapas.push(...data.results);
      });
    },
    getIdeas() {
      let endpoint = "/api/idea/";
      apiService(endpoint).then(data => {
        this.ideas.push(...data.results);
      });
    }
  },
  created() {
    this.getPersonas();
    this.getEtapas();
    this.getIdeas();
  }
};
</script>
