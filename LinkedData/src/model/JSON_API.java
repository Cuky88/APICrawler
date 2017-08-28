package model;

/**
 * Created by Jan-Peter on 04.06.2017.
 */
public class JSON_API {

    String name;
    String homepage;
    String blog;
    String endpoint;
    String URI;
    String keywords;

    String pwDescr;
    String blogDescr;
    String ldDescr;

    String error="-";
    Boolean improved=false;
    String improvedURL="";
    Boolean improveSuccess =false;
    Boolean deprecated = false;


    String body;


    public static int counter = 0;
    public static int counterImproved = 0;

    public JSON_API() {
    }

    public JSON_API(String name, String homepage, String blog, String endpoint) {
        this.name = name;
        this.homepage = homepage;
        this.blog = blog;
        this.endpoint = endpoint;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getHomepage() {
        return homepage;
    }

    public void setHomepage(String homepage) {
        this.homepage = homepage;
    }

    public String getBlog() {
        return blog;
    }

    public void setBlog(String blog) {
        //System.out.println("Set blog to\"" + blog +"\"");
        this.blog = blog;
    }

    public String getEndpoint() {
        return endpoint;
    }

    public void setEndpoint(String endpoint) {
        this.endpoint = endpoint;
    }

    public String getPwDescr() {
        return pwDescr;
    }

    public void setPwDescr(String pwDescr) {
        this.pwDescr = pwDescr;
    }

    public String getBlogDescr() {
        return blogDescr;
    }

    public void setBlogDescr(String blogDescr) {
        this.blogDescr = blogDescr;
    }

    public String getLdDescr() {
        return ldDescr;
    }

    public void setLdDescr(String ldDescr) {
        this.ldDescr = ldDescr;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public String getURI() {
        return URI;
    }

    public void setURI(String URI) {
        this.URI = URI;
    }

    public String getKeywords() {
        return (keywords==null) ? ("") : (keywords);
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public String getError() {
        return error;
    }

    public Boolean isImproved() {
        return improved;
    }

    public void setImproved(Boolean improved) {
        this.improved = improved;
    }

    public String getImprovedURL() {
        return improvedURL;
    }

    public void setImprovedURL(String improvedURL) {
        this.improvedURL = improvedURL;
    }

    public void setError(String error) {
        this.error = error;
    }

    public Boolean isImproveSuccess() {
        return improveSuccess;
    }

    public void setImproveSuccess(Boolean improveSuccess) {
        this.improveSuccess = improveSuccess;
    }

    public Boolean isDeprecated() {
        return deprecated;
    }

    public void setDeprecated(Boolean deprecated) {
        this.deprecated = deprecated;
    }

    @Override
    public String toString() {
        if(!this.homepage.equals("") || !this.getBlog().equals("")) {

            counter++;
            return this.name + ": HP: " + this.homepage + ", Blog: " + this.blog;

        } else {
            return "---";
        }
    }

    public String getSelcukJSON() {

        String json = "  {\n     \"progweb_url\": \"" + getHomepage() + "\",\n     \"api_url_full\": \"" + (getImprovedURL().equals("") ? (getBlog()) : (getImprovedURL())) + "\",\n     \"website_descr\": \"" + getBody() + "\",\n     \"api_name\": \"" + getName() + "\",\n     \"website_keywords\":\"" + getKeywords() +"\"\n  }, ";

        return json;

    }
}
