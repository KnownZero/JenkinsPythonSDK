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
        pass
        # @classmethod
        # def UsernamePassword(cls, domain: str, cred_id: str, username: str, password: str) -> str:
        #     """
        #     Create a new Username/Password credential.
        #
        #     :return: The newly created Username/Password credential template.
        #     :rtype: str
        #     """
        #     # TODO: This
        #     return Builder._Templates.Credentials.UsernamePassword.format(domain=domain, cred_id=cred_id,
        #                                                                   username=username, password=password)

    @classmethod
    def User(cls, /, *,
             username: str,
             password: str,
             cred_id=None,
             domain: str = "GLOBAL") -> ...:
        # TODO: This
        raise NotImplemented

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
