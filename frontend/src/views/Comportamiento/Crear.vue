<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Crear Comportamiento</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'listar_comportamiento' }"
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
              <label>Persona</label>
              <select
                id="persona"
                class="form-control"
                v-model="CMP_Persona_Comportamiento"
                required
                disabled
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
            <div class="form-group ">
              <label>Describe sus hábitos y su día a día</label>
              <br />
              <textarea
                id="descripcion"
                class="form-control"
                aria-label="With textarea"
                v-model="CMP_Descripcion_Comportamiento"
              ></textarea>
            </div>
            <div class="form-group ">
              <label>
                ¿Cuáles son los medios de comunicación usados por tu Persona?
              </label>
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
                          <i class="fa " v-bind:class="md.MDO_Icono_Medio"></i>
                          {{ md.MDO_Nombre_Medio }}
                        </label>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
            <router-link
              :to="{ name: 'listar_comportamiento' }"
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
      CMP_Persona_Comportamiento: this.id,
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
        this.obtenerUltimoComportamiento();
        this.obtenerUltimoComportamiento();
        this.medios.forEach(medio => {
          if (
            document.getElementById("medio" + medio.MDO_Id_Medio).checked ==
            true
          ) {
            alert(this.comportamiento[0].CMP_Id_Comportamiento);
            alert(medio.MDO_Id_Medio);
            let endpoint = "/api/comportamiento-medio/";
            let method = "POST";
            apiService(endpoint, method, {
              CMP_MDO_Comportamiento_Id: this.comportamiento[0]
                .CMP_Id_Comportamiento,
              CMP_MDO_Medio_Id: medio.MDO_Id_Medio
            });
          }
        });
        this.$router.push({ name: "listar_comportamiento" });
      }
    },
    guardarComportamiento() {
      let endpoint = "/api/comportamiento/";
      let method = "POST";
      apiService(endpoint, method, {
        CMP_Descripcion_Comportamiento: this.CMP_Descripcion_Comportamiento,
        CMP_Persona_Comportamiento: this.CMP_Persona_Comportamiento
      });
    },
    obtenerUltimoComportamiento() {
      let endpoint = "/api/comportamiento-ultimo/";
      apiService(endpoint).then(data => {
        this.comportamiento.push(...data.results);
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
.custom-control-input:checked ~ .custom-control-label::before {
  color: #fff;
  border-color: rgb(52, 70, 117);
  background-color: rgb(52, 70, 117);
}
</style>
