function Component()
{
    // default constructor
}

Component.prototype.createOperations = function()
{
	// call default implementation to actually install files
	component.createOperations();

	if (systemInfo.productType === "windows") {
		component.addOperation("Execute", "@TargetDir@/vc2013_vcredist_x64.exe", "/q");
		component.addOperation("Execute", "@TargetDir@/vc2015_vcredist_x64.exe", "/q");
		component.addOperation("Delete", "@TargetDir@/vc2013_vcredist_x64.exe");
		component.addOperation("Delete", "@TargetDir@/vc2015_vcredist_x64.exe");
	}
}
