<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Proyectos</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'crear_proyecto' }"
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
                <th scope="col">Nombre del proyecto</th>
                <th scope="col">Empresa</th>
                <th scope="col">Persona</th>
                <th scope="col">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(pry, index) in proyectos" :key="pry.PRY_Id_Proyecto">
                <th scope="row">
                  {{ ++index }}
                </th>
                <td>
                  {{ pry.PRY_Nombre_Proyecto }}
                </td>
                <td>
                  {{ pry.PRY_Empresa_Proyecto.EMP_Nombre_Empresa }}
                </td>
                <td>
                  {{
                    pry.PRY_Persona_Proyecto.PSN_Nombres_Persona +
                      " " +
                      pry.PRY_Persona_Proyecto.PSN_Apellidos_Persona
                  }}
                </td>
                <td>
                  <router-link
                    :to="{
                      name: 'editar_proyecto',
                      params: { id: pry.PRY_Id_Proyecto }
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
                    @click="deleteProyecto(pry.PRY_Id_Proyecto)"
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
            <p v-show="loadingProyectos">...Cargando...</p>
            <button
              v-show="nextProyecto"
              @click="getProyectos('MAS')"
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
  data() {
    return {
      proyectos: [],
      nextProyecto: null,
      loadingProyectos: false
    };
  },
  methods: {
    getProyectos(accion = null) {
      let endpoint = "/api/proyecto-join/";
      if (accion == "DELETE") {
        this.proyectos = [];
        apiService(endpoint).then(data => {
          this.proyectos.push(...data.results);
        });
      } else {
        if (this.nextProyecto) {
          endpoint = this.nextProyecto;
        }
        this.loadingProyectos = true;
        apiService(endpoint).then(data => {
          this.proyectos.push(...data.results);
          this.loadingProyectos = false;
          if (data.next) {
            this.nextProyecto = data.next;
          } else {
            this.nextProyecto = null;
          }
        });
      }
    },
    async deleteProyecto(proyecto) {
      let endpoint = `/api/proyecto/${proyecto}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getProyectos("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    }
  },
  created() {
    this.getProyectos();
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
