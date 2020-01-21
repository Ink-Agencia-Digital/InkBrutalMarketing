<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Proyecto</h1>
      <br />
      <router-link :to="{ name: 'crear_proyecto' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
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
          <tr v-for="pry in proyectos" :key="pry.PRY_Id_Proyecto">
            <th scope="row">
              {{ pry.PRY_Id_Proyecto }}
            </th>
            <td>
              <label>
                {{ pry.PRY_Nombre_Proyecto }}
              </label>
            </td>
            <td>
              <label>
                {{ pry.PRY_Empresa_Proyecto.EMP_Nombre_Empresa }}
              </label>
            </td>
            <td>
              <label>
                {{
                  pry.PRY_Persona_Proyecto.PSN_Nombres_Persona +
                    " " +
                    pry.PRY_Persona_Proyecto.PSN_Apellidos_Persona
                }}
              </label>
            </td>
            <td>
              <router-link
                :to="{
                  name: 'editar_proyecto',
                  params: { id: pry.PRY_Id_Proyecto }
                }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button
                type="button"
                class="bpn btn-danger"
                @click="deleteProyecto(pry.PRY_Id_Proyecto)"
              >
                Eliminar
              </button>
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
