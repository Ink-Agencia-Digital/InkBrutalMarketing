<template>
  <div class="container">
    <div class="col-md-8">
      <form @submit.prevent="onSubmit">
        <br /><br />
        <h1>Comportamiento</h1>
        <br />
        <div class="form-group">
          <h3>Persona</h3>
          <select
            id="persona"
            class="form-control"
            v-model="CMP_Persona_Comportamiento"
            required
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
        <div class="form-group ">
          <h4>Describe sus hábitos y su día a día</h4>
          <br />
          <h5 for="descripcion">Descripción</h5>
          <textarea
            id="descripcion"
            class="form-control"
            aria-label="With textarea"
            v-model="CMP_Descripcion_Comportamiento"
          ></textarea>
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
                      :id="'medio' + md.MDO_Id_Medio"
                      :value="md.MDO_Id_Medio"
                      v-model="CMP_MDO_Medio_Id"
                    />
                    <label
                      class="custom-control-label"
                      :for="'medio' + md.MDO_Id_Medio"
                    >
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
        <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
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
      medios: [],
      valMedio: false,
      comportamiento: [],
      idComportamiento: null,
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
    getMedios() {
      let endpoint = "/api/medio/";
      apiService(endpoint).then(data => {
        this.medios.push(...data.results);
      });
    },
    onSubmit() {
      this.medios.forEach(medio => {
        if (
          document.getElementById("medio" + medio.MDO_Id_Medio).checked == true
        ) {
          this.valMedio = true;
        }
      });
      if (!this.CMP_Persona_Comportamiento) {
        this.error = "Por favor seleccione una persona";
      } else if (!this.CMP_Descripcion_Comportamiento) {
        this.error = "Por favor digite una descripción";
      } else if (!this.valMedio) {
        this.error = "Por favor seleccione almenos un medio";
      } else {
        this.guardarComportamiento();
        /*this.obtenerUltimoComportamiento();
        this.comportamiento.forEach(cmp => {
          this.medios.forEach(medio => {
            if (
              document.getElementById("medio" + medio.MDO_Id_Medio).checked ==
              true
            ) {
              let endpoint = "/api/comportamiento-medio/";
              let method = "POST";
              apiService(endpoint, method, {
                CMP_MDO_Comportamiento_Id: cmp.CMP_Id_Comportamiento,
                CMP_MDO_Medio_Id: medio.MDO_Id_Medio
              });
            }
          });
        });*/
      }
    },
    guardarComportamiento() {
      let endpoint = "/api/comportamiento/";
      let method = "POST";
      apiService(endpoint, method, {
        CMP_Descripcion_Comportamiento: this.CMP_Descripcion_Comportamiento,
        CMP_Persona_Comportamiento: this.CMP_Persona_Comportamiento
      }).then(data => {
        this.comportamiento.push(...data.results);
      });
    },
    obtenerUltimoComportamiento() {
      let endpoint = "/api/comportamiento-ultimo/";
      apiService(endpoint);
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
.custom-control-input:checked ~ .custom-control-label::before {
  color: #fff;
  border-color: rgb(52, 70, 117);
  background-color: rgb(52, 70, 117);
}
</style>
