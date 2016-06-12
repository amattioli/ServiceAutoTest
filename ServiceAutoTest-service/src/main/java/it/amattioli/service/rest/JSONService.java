package it.amattioli.service.rest;

import javax.naming.InitialContext;
import javax.sql.DataSource;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Response;

import static javax.ws.rs.core.MediaType.APPLICATION_JSON;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.HashMap;
import java.util.Map;

@Path("json")
public class JSONService {

	@GET
    @Produces(APPLICATION_JSON)
    @Path("/info")
	public Response getInfo() throws Exception {
		Map<String, Object> body = new HashMap<String, Object>();
		InitialContext iniCtx = new InitialContext();
		DataSource datasource = (DataSource)iniCtx.lookup("jdbc/serviceAutoTestDb");
		Connection conn = null;
        try {
            conn = datasource.getConnection();
            PreparedStatement stmt = conn.prepareStatement("select attr1,attr2 from service");
            ResultSet rs = stmt.executeQuery();
            if(rs.next()){
                String attr1 = rs.getString(1);
                String attr2 = rs.getString(2);
                body.put("attr1", attr1);
        		body.put("attr2", attr2);
            }
        } finally {
            if (conn != null) {
                conn.close();
            }
        }
		return Response.status(200).entity(body).build();
	}

}
