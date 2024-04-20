__all__ = ["HTTP_RETRY_COUNT", "HOST_MATCH_REGEX_PATTERN", "HTTP_HEADER_DEFAULT", "Endpoints",
           "XML_HEADER_DEFAULT", "FORM_HEADER_DEFAULT", "XML_POST_HEADER", "Class",
           "FORM_MULTIPART_HEADER"]

HTTP_RETRY_COUNT = 1
HTTP_HEADER_DEFAULT = {"Content-Type": "application/json"}
XML_HEADER_DEFAULT = {"Content-Type": "application/xml"}
XML_POST_HEADER = {"Content-Type": "text/xml"}
FORM_HEADER_DEFAULT = {"Content-Type": "application/x-www-form-urlencoded"}
FORM_MULTIPART_HEADER = {"Content-Type": "multipart/form-data"}

HOST_MATCH_REGEX_PATTERN = r"^[a-zA-Z0-9.-]+$"


class Endpoints:
    class Instance:
        Crumb = "crumbIssuer/api/json"
        Connect = "login"
        # Jobs = "api/json?tree="  # TODO: Change ?tree= maybe?
        Standard = "api/json"
        About = "about"  # For plugins list etc
        OverallLoad = "overallLoad/api/json"

    class Manage:
        Reload = "#"
        CredentialStore = "manage/credentials/store/system"

    class Jobs:
        Create = "createItem"
        Enable = "enable"
        Disable = "disable"
        Xml = "config.xml"
        Iter = "jobs[fullName,url,jobs[fullName,url,jobs]]"

    class Builds:
        BuildNumber = "buildNumber"
        BuildConsoleText = "consoleText"
        ProgressiveConsoleText = "progressiveText"
        ProgressiveHtml = "progressiveHtml"
        Delete = "doDelete"
        Changes = "changes"
        Build = "build"
        buildWithParameters = "buildWithParameters"
        RebuildLast = "lastCompletedBuild/rebuild"
        RebuildCurrent = "rebuild"

    class Views:
        View = "view"
        Create = "createView"
        Iter = "views[name,url,jobs[fullName,url,jobs]]"
        Delete = "doDelete"

    class Credential:
        Create = "createCredentials"
        Get = "credential/{cred_id}"
        Move = "doMove"

    class Credentials:
        Domain = "manage/credentials/store/system/domain/{domain}"
        Create = "manage/credentials/store/system/newDomain"
        CreateDomain = "manage/credentials/store/system/createDomain"

    class Maintenance:
        Restart = "restart"
        SafeRestart = "safeRestart"
        QuietDown = "quietDown"
        NoQuietDown = "cancelQuietDown"
        Shutdown = "exit"
        SafeShutdown = "safeExit"

    class Users:
        List = "asynchPeople"
        User = "user/{username}"
        Create = "manage/securityRealm/addUser"
        CreateByAdmin = "/securityRealm/createAccountByAdmin"

    class User:
        Logout = "logout"
        Delete = "doDelete"
        Builds = "builds"
        Views = "my-views/view/all"
        Credentials = "credentials/store/user/domain/{domain}/"
        Me = "me"
        Boot = "user/{user}/descriptorByName/jenkins.security.seed.UserSeedProperty/renewSessionSeed"

    class Plugins:
        PluginManager = "pluginManager"
        UpdateCenter = "updateCenter"
        UpdateCenterIter = "sites[{p_type}[*[*]]{paginate}]"
        PluginManagerIter = "{p_type}[*[*]]{paginate}"
        Upload = "pluginManager/uploadPlugin"
        Install = "installNecessaryPlugins"
        Enable = "plugin/{plugin}/makeEnabled"
        Disable = "plugin/{plugin}/makeDisabled"
        Uninstall = "plugin/{plugin}/doUninstall"

    class UpdateCenter:
        Iter = "sites[id]"
        Site = "updateCenter/site/{site}"

    class Nodes:
        Computer = "computer"
        Node = "computer/{name}"
        Delete = "doDelete"
        Disable = "toggleOffline"
        Create = "doCreateItem"


class Class:
    Folder = "com.cloudbees.hudson.plugins.folder.Folder"
    Freestyle = "hudson.model.FreeStyleProject"
    JenkinsFile = ""
    ListView = "hudson.model.ListView"
    MyView = "hudson.model.MyView"
    Dashboard = "hudson.plugins.view.dashboard.Dashboard"
    UsernamePassword = ""


# class References:
#     class Jobs:
#         JOBS = "jobs"
#         VIEWS = "views"
