<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Comportamientos</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'crear_comportamiento' }"
                class="btn btn-info"
              >
                <i class="material-icons" style="color:white;">add</i>Crear
              </router-link>
            </li>
          </ul>
        </div>
        <div class=" body table-responsive">
          <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
          <table class="table">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Persona</th>
                <th scope="col">Descripción</th>
                <th scope="col">Medios</th>
                <th scope="col">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(cmp, index) in comportamientos"
                :key="cmp.CMP_Id_Comportamiento"
              >
                <th scope="row">
                  {{ ++index }}
                </th>
                <td>
                  <label class="" for="persona">
                    {{
                      cmp.CMP_Persona_Comportamiento.PSN_Nombres_Persona +
                        " " +
                        cmp.CMP_Persona_Comportamiento.PSN_Apellidos_Persona
                    }}
                  </label>
                </td>
                <td>
                  <label class="" for="descripcion">
                    {{ cmp.CMP_Descripcion_Comportamiento }}
                  </label>
                </td>
                <td>
                  <button @click="getMedios(cmp.CMP_Id_Comportamiento)">
                    Mostrar
                  </button>
                  <div
                    :id="'medios' + cmp.CMP_Id_Comportamiento"
                    style="display: none;"
                  >
                    <li v-for="mdo in medios" :key="mdo.MDO_iD_Medio">
                      {{ mdo.MDO_Nombre_Medio }}
                    </li>
                  </div>
                </td>
                <td>
                  <router-link
                    :to="{
                      name: 'editar_comportamiento'
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
      comportamientos: [],
      nextComportamiento: null,
      loadingComportamientos: false,
      medios: [],
      divMedios: null
    };
  },
  methods: {
    getComportamientos(accion = null) {
      let endpoint = "/api/comportamiento-join/";
      if (accion == "DELETE") {
        this.comportamientos = [];
        apiService(endpoint).then(data => {
          this.comportamientos.push(...data.results);
        });
      } else {
        if (this.nextComportamiento) {
          endpoint = this.nextComportamiento;
        }
        this.loadingComportamientos = true;
        apiService(endpoint).then(data => {
          this.comportamientos.push(...data.results);
          this.loadingComportamientos = false;
          if (data.next) {
            this.nextComportamiento = data.next;
          } else {
            this.nextComportamiento = null;
          }
        });
      }
    },
    async deleteComportamiento(comportamiento) {
      let endpoint = `/api/comportamiento/${comportamiento}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getComportamientos("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    },
    getMedios(comportamiento) {
      this.divMedios = document.getElementById(
        "medios" + comportamiento
      ).style.display;
      if (this.divMedios == "block") {
        document.getElementById("medios" + comportamiento).style.display =
          "none";
      } else {
        let endpoint = `/api/persona/${comportamiento}/medio/`;
        this.medios = [];
        apiService(endpoint).then(data => {
          this.medios.push(...data.results);
        });
        document.getElementById("medios" + comportamiento).style.display =
          "block";
      }
    }
  },
  created() {
    this.getComportamientos();
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
