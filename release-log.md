# Release log

## Release (Minor/Fixes) 1.4.4 - 11/12/2024
### Fixes:
- Fix HTTPX deprecated proxies parameter

### New:
- Small cleanup of HTTPX core code
- No py3.8 support

###

## Release (Minor/Fixes) 1.4.3 - 12/08/2024
### Fixes:
- Suppress httpx warning when posting data
- Readthedocs examples page was too big, and it wasn't loading properly on readthedocs site

### New:
- Reduced requirements (removed):
  - orjson
  - pydantic

###

## Release (Minor/Fixes) 1.4.2 - 07/07/2024
### Fixes:
- Fix console logs broken json
- Fix Build 'Done' status for older Jenkins versions
- Removed blocking thread from Quiet Mode

### New:
- Remove redundant folder copy parameter
- Major unit testing added
- Queue newest/oldest now returns an object

###

## Release (Minor/Fixes) 1.4.1 - 05/07/2024
### Fixes:
- Import error in \_\_init\_\_.py

### New:
- Specifying package versions
- Only support 3.7+ now

###

## Release (Minor/Fixes) 1.4.0 - 04/07/2024
### Fixes:
- Jenkins version endpoint which didn't work with old versions
- Folder type in folder create methods
- Refactor http methods to fix 403 errors
- Removed HttpUrl, which was causing issues
- Code cleanup

### New:
- New testing setup script
- Testing of many LTS versions
- Removed many mini sessions in favour of one single session

###

## Release (Minor/Fixes) 1.3.9 - 13/06/2024
### Fixes:
- Checking people-view plugin is installed for Jenkins v2.452+

### New:
- Adding build filter options
  - lastStableBuild
  - lastSuccessfulBuild
  - lastFailedBuild
  - lastUnsuccessfulBuild
  - lastCompletedBuild

###

## Release (Minor/Fixes) 1.3.8 - 05/06/2024
### Fixes:
- Code readability
- Connect method

### New:
- Adding progressive build console output (params previously did nothing)

###

## Release (Minor/Fixes) 1.3.5 - 10/05/2024
### Fixes:
- Fix import errors in lower py versions

### New:
- Ability to create more jobs:
  - Pipeline
  - Multi-configuration project
  - MultiBranchPipeline
  - OrganizationFolder

###

## Release (Minor/Fixes) 1.3.2 - 08/05/2024
### Fixes:
- Fix documentation inaccuracies

### New:
- Functionality to configure new update center sites
- Run commands in the script console
- Upload plugins functionality

###

## Release (Minor/Fixes) 1.3 - 21/04/2024
### Fixes:
- Fix documentation links + some examples using Builder
- Fix views pagination
- Replaced exceptions - JenkinsJobNotFound and JenkinsFolderNotFound with generic JenkinsNotFound
- General functionality fixes

### New:
- new JenkinsBaseException is now a catchall for all Jenkins exceptions
- Added Workspace module
- Added Queue module


## Release (Major/Fixes) 1.2 - 20/04/2024
### Fixes:
- General cleanup
- Fixed Build.oldest()
- Some actions were called as properties

### New:
- Improved documentation
- Improved error handling
- Added timestamp to Build
- Added build parameters & delay to Build
- Added Build.next(), Build.previous() functionality
- Added Rebuild options in Build/Builds
- Added Plugins functionality (Beta)
- Added Nodes module
- Added UpdateCenter class with Site interation

## Release (Minor/Fixes) 1.0.2 - 14/04/2024
### Fixes:
- Pydantic validation error for some hosts when connecting
- Fixing View documentation
- Fixing View class helpers
- Fixing pagination returning one duplicate

### New:
- Adding Me documentation
- Adding release-log.md

###

## Release (Major) 1.0 - 14/04/2024
### First release - includes all major code

### Fixes:
- None

### New:
- System
- Users
- Credential store
  - Domains
  - Credentials
- Me
- Jobs
- Folders
- Views
- Builds
- Builder
