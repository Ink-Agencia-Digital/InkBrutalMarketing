<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Comportamiento</h1>
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
        <div class="form-group ">
          <h4>Describe sus hábitos y su día a día</h4>
          <br />
          <h5 for="descripcion">Descripción</h5>
          <textarea class="form-control" aria-label="With textarea"></textarea>
        </div>
        <br /><br />
        <div class="form-group ">
          <h4>¿Cuáles son los medios de comunicación usados por tu Persona?</h4>
          <br />
          <h5 for="medio">Medios</h5>
          <br />
          <div class="custom-control custom-switch">
            <div class="row">
              <div class="col">
                <ul>
                  <li v-for="md in medios" :key="md.MDO_Id_Medio">
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio1"
                      :value="md.MDO_Id_Medio"
                    />
                    <label class="custom-control-label" for="medio1">
                      {{ md.MDO_Nombre_Medio }}
                    </label>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="otro">Otros</label>
            <input
              type="text"
              class="form-control"
              id="otro"
              placeholder="¿Cúal otro medio?"
            />
          </div>
        </div>
        <br />
        <button
          type="submit"
          class="btn btn-dark"
          style="background-color: #344675;"
        >
          Guardar
        </button>
        <br /><br /><br />
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
      medios: []
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    getMedios() {
      let endpoint = "/api/medio/";
      apiService(endpoint).then(data => {
        this.medios.push(...data.results);
      });
    }
  },
  created() {
    this.getPersonas();
    this.getMedios();
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
