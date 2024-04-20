__all__ = ["Builder"]


class Builder:
    """
    Easy builder if you don't like XML... like me ;)
    """

    @classmethod
    def Folder(cls, name, description: str):
        """
        Create a new folder template.

        :param name: The name of the folder.
        :type name: str
        :param description: The description of the folder.
        :type description: str
        :return: The newly created folder template.
        :rtype: Folder
        """
        template = cls._Templates.Folder.format(folder_name=name, description=description)
        return template

    @classmethod
    def Freestyle(cls):
        """
        Create a new Freestyle job.

        :return: The newly created Freestyle job template.
        :rtype: Job
        """
        # TODO: This
        raise NotImplemented

    @classmethod
    def View(cls):
        """
        Create a new view template.

        :return: The newly created view.
        :rtype: View
        """
        raise NotImplemented

    class Credentials:
        @classmethod
        def UsernamePassword(cls, *,
                             domain: str = "GLOBAL",
                             cred_id: str,
                             username: str,
                             password: str) -> ...:
            """
            Create a new Username/Password credential.

            :return: The newly created Username/Password credential template.
            :rtype: str
            """
            # TODO: Domain param should be forced in Domain
            return Builder._Templates.Credentials.UsernamePassword.format(domain=domain, cred_id=cred_id,
                                                                          username=username, password=password)

        @classmethod
        def Domain(cls, *,
                   name: str,
                   description: str = "",
                   includes: list = None,
                   excludes: list = None) -> ...:
            includes = ",".join(includes) if includes else ""
            excludes = ",".join(excludes) if excludes else ""
            return Builder._Templates.Credentials.Domain.format(name=name, description=description,
                                                                includes=includes, excludes=excludes)

    @classmethod
    def User(cls, *,
             username: str,
             password: str,
             fullname: str,
             email: str) -> ...:
        return {
            'username': username,
            'password1': password,
            'password2': password,
            'fullname': fullname,
            'email': email
        }

    @classmethod
    def Node(cls,
             description: str,
             remote_fs: str,
             executors: int = 1,
             label: str = "",
             mode: str = "NORMAL"):
        node = {
            'nodeDescription': description,
            'numExecutors': executors,
            'remoteFS': remote_fs,
            'labelString': label,
            'mode': mode,
            'retentionStrategy': {
                'stapler-class': 'hudson.slaves.RetentionStrategy$Always'
            },
            'nodeProperties': {'stapler-class-bag': 'true'},
            'launcher': {'stapler-class': 'hudson.slaves.JNLPLauncher'}
        }
        return node

    class _Templates:
        Folder = \
        """<com.cloudbees.hudson.plugins.folder.Folder>
            <name>{folder_name}</name>
            <description>{description}</description>
        </com.cloudbees.hudson.plugins.folder.Folder>
        """

        Freestyle = \
        """<project>
              <description>{description}</description>
              <keepDependencies>false</keepDependencies>
              <properties/>
              <scm class="hudson.scm.NullSCM"/>
              <canRoam>true</canRoam>
              <disabled>{disabled}</disabled>
              <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
              <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
              <triggers/>
              <concurrentBuild>false</concurrentBuild>
              <builders/>
              <publishers/>
              <buildWrappers/>
            </project>"""

        View = """
        
        """

        class Credentials:
            UsernamePassword = \
            """<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
                <scope>{domain}</scope>
                <id>{cred_id}</id>
                <username>{username}</username>
                <password>{password}</password>
               </com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>"""

            Domain = \
            """<com.cloudbees.plugins.credentials.domains.Domain>
              <name>{name}</name>
              <description>{description}</description>
              <specifications>
                <com.cloudbees.plugins.credentials.domains.HostnameSpecification>
                  <includes>{includes}</includes>
                  <excludes>{excludes}</excludes>
                </com.cloudbees.plugins.credentials.domains.HostnameSpecification>
              </specifications>
            </com.cloudbees.plugins.credentials.domains.Domain>"""
