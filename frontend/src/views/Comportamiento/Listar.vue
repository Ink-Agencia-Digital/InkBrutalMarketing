<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Comportamiento</h1>
      <br />
      <router-link :to="{ name: 'crear_comportamiento' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
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
          <tr v-for="cmp in comportamientos" :key="cmp.CMP_Id_Comportamiento">
            <th scope="row">
              {{ cmp.CMP_Id_Comportamiento }}
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
                :to="{ name: 'editar_comportamiento' }"
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
