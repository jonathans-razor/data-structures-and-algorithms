/*

Create a JavaScript program the can solve the following problem. Enable this program to be run from the command line and automatically pass in the data on the command line.

We want to be able to determine the top 100 most frequently deployed software packages across our web services environments. Assume that our software deployment system will invoke a method providing the software package name whenever it deploys a software package.

Given the example method signature below as a starting point and using JavaScript, provide an implementation for the two methods.

Example Method Signatures:

void recordDeployment(String softwarePackageName)
{
}

List<String> getTop100Deployments();
{

}

Example Deployment Inputs:

Package1
Package2
Package3
Package44
Package44
Package44
Package3
Package3
Package3
Package9
Package17
Package18
Package18
Package26
Package109

Example Expected Output:

[Package3, Package44, Package18 . . .]

*/

class DeploymentTracker {
    constructor() {
        this.deploymentCounts = new Map();
    }

    recordDeployment(softwarePackageName) {
        if (!this.deploymentCounts.has(softwarePackageName)) {
            this.deploymentCounts.set(softwarePackageName, 1);
        } else {
            this.deploymentCounts.set(softwarePackageName, this.deploymentCounts.get(softwarePackageName) + 1);
        }
    }

    getTop100Deployments() {
        const sortedDeployments = [...this.deploymentCounts.entries()]
            .sort((a, b) => b[1] - a[1])
            .map(entry => entry[0])
            .slice(0, 100);

        return sortedDeployments;
    }
}

// Example usage
const deploymentTracker = new DeploymentTracker();
const commandLineInputs = process.argv.slice(2); // Get command line arguments excluding "node" and script name

commandLineInputs.forEach(packageName => deploymentTracker.recordDeployment(packageName));
const top100Deployments = deploymentTracker.getTop100Deployments();
console.log(top100Deployments);