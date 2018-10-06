var SMContract = artifacts.require("./SMContract.sol");

module.exports = function(deployer) {
  deployer.deploy(SMContract);
};
