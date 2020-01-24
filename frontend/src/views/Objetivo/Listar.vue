<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Objetivos y desafios</h1>
      <br />
      <router-link :to="{ name: 'crear_objetivo' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
      <select
        id="persona"
        class="form-control"
        v-model="idPersona"
        @change="onChange($event)"
      >
        <option selected value="">--Seleccione una Persona--</option>
        <option
          v-for="psn in personas"
          :key="psn.PSN_Id_Persona"
          :value="psn.PSN_Id_Persona"
        >
          {{ psn.PSN_Nombres_Persona + " " + psn.PSN_Apellidos_Persona }}
        </option>
      </select>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Persona</th>
            <th scope="col">Pregunta</th>
            <th scope="col">Respuesta</th>
            <th scope="col">Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="obj in objetivos" :key="obj.OBJ_Id_Objetivo">
            <th scope="row">
              {{ obj.OBJ_Id_Objetivo }}
            </th>
            <td>
              <label class="" for="persona">
                {{
                  obj.OBJ_Persona_Objetivo.PSN_Nombres_Persona +
                    " " +
                    obj.OBJ_Persona_Objetivo.PSN_Apellidos_Persona
                }}
              </label>
            </td>
            <td>
              <label class="" for="descripcion">
                {{ obj.OBJ_Pregunta_Objetivo.PRG_Nombre_Pregunta }}
              </label>
            </td>
            <td>
              <label class="" for="medios">
                {{ obj.OBJ_Respuesta_Objetivo }}
              </label>
            </td>
            <td>
              <router-link
                :to="{
                  name: 'editar_objetivo',
                  params: { id: obj.OBJ_Id_Objetivo }
                }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      personas: [],
      objetivos: [],
      nextObjetivo: null,
      loadingObjetivos: false
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    onChange() {
      this.getObjetivos(event.target.value);
    },
    getObjetivos(accion = null) {
      if (accion == null || accion == "") {
        let endpoint = "/api/objetivo-join/";
        this.objetivos = [];
        apiService(endpoint).then(data => {
          this.objetivos.push(...data.results);
        });
      } else if (accion == "DELETE") {
        let endpoint = "/api/objetivo-join/";
        this.objetivos = [];
        if (this.nextObjetivo) {
          endpoint = this.nextObjetivo;
        }
        this.loadingObjetivos = true;
        apiService(endpoint).then(data => {
          this.objetivos.push(...data.results);
          this.loadingObjetivos = false;
          if (data.next) {
            this.nextObjetivo = data.next;
          } else {
            this.nextObjetivo = null;
          }
        });
      } else {
        let endpoint = `/api/persona/${accion}/objetivo/`;
        this.objetivos = [];
        if (this.nextObjetivo) {
          endpoint = this.nextObjetivo;
        }
        this.loadingObjetivos = true;
        apiService(endpoint).then(data => {
          this.objetivos.push(...data.results);
          this.loadingObjetivos = false;
          if (data.next) {
            this.nextObjetivo = data.next;
          } else {
            this.nextObjetivo = null;
          }
        });
      }
    },
    async deleteObjetivo(proyecto) {
      let endpoint = `/api/objetivo/${proyecto}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getObjetivos("DELETE", null);
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    }
  },
  created() {
    this.getObjetivos();
    this.getPersonas();
  }
};
</script>

<style>
.b {
  padding: 2% 3%;
  text-align: center;
  font-size: 16px;
  border-radius: 8px;
}
.bp {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
.bpn {
  padding: 2% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
