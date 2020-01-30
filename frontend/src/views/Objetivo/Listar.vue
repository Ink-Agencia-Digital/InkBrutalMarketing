<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Objetivos</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'crear_objetivo' }"
                class="btn btn-info"
              >
                <i class="material-icons" style="color:white;">add</i>Crear
              </router-link>
              &nbsp;
              <router-link
                :to="{ name: 'listar_persona' }"
                class="btn btn-danger"
              >
                <i class="material-icons" style="color:white;"
                  >keyboard_backspace</i
                >
                Volver a Personas
              </router-link>
            </li>
          </ul>
        </div>
        <div class=" body table-responsive">
          <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
          <br />
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
              <tr v-for="(obj, index) in objetivos" :key="obj.OBJ_Id_Objetivo">
                <th scope="row">
                  {{ ++index }}
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
                    title="Editar este Registro"
                  >
                    <i
                      class="material-icons text-info"
                      style="font-size: 20px;"
                    >
                      edit
                    </i>
                  </router-link>
                  <button
                    type="button"
                    class="btn-accion-tabla"
                    title="Eliminar este Registro"
                  >
                    <i
                      class="material-icons text-danger"
                      style="font-size: 20px;"
                    >
                      delete
                    </i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="my-4">
            <p v-show="loadingComportamientos">...Cargando...</p>
            <button
              v-show="nextComportamiento"
              @click="getComportamientos('MAS')"
              class="btn btn-sm btn-outline-success"
            >
              Cargar Más
            </button>
          </div>
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
      personas: [],
      objetivos: [],
      nextObjetivo: null,
      loadingObjetivos: false,
      idPersona: ""
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    getObjetivos(accion = null) {
      if (accion == null || accion == "") {
        let endpoint = `/api/persona/${this.id}/objetivo/`;
        this.objetivos = [];
        apiService(endpoint).then(data => {
          this.objetivos.push(...data.results);
        });
      } else if (accion == "DELETE") {
        let endpoint = `/api/persona/${this.id}/objetivo/`;
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
        let endpoint = `/api/persona/${this.id}/objetivo/`;
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
