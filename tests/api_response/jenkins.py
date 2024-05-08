
__all__ = ["Endpoints"]


class Endpoints:
    class Instance:
        Crumb = {"_class":"hudson.security.csrf.DefaultCrumbIssuer","crumb":"369cc2704feaf8421211cafce8060424602d497bffd490b5a0539cf6e8a41b3f","crumbRequestField":"Jenkins-Crumb"}
        Connect = "login"
        Standard = "api/json"
        OverallLoad = "overallLoad"

    class Manage:
        Reload = "#"
        CredentialStore = "manage/credentials/store/system"

    class Jobs:
        Create = "createItem"
        Enable = "enable"
        Disable = "disable"
        Xml = "config.xml"
        Iter = "jobs[fullName,url,jobs[fullName,url,jobs]]"

    class Workspace:
        Download = "ws/*zip*/{name}.zip"
        DownloadFile = "ws/{path}"
        Wipe = "doWipeOutWorkspace"

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

    class Queue:
        Queue = "queue"
        QueueIter = "items[*,task[url,fullName,nextBuildNumber]]{paginate}"

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
