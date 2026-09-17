REQUIRED_LABELS={"app.kubernetes.io/name","app.kubernetes.io/version"}
def validate_deployment(manifest):
    metadata=manifest.get("metadata",{}); spec=manifest.get("spec",{})
    labels=metadata.get("labels",{})
    if manifest.get("kind") != "Deployment": raise ValueError("only Deployment manifests are supported")
    if not REQUIRED_LABELS <= labels.keys(): raise ValueError("required workload labels missing")
    containers=spec.get("template",{}).get("spec",{}).get("containers",[])
    if not containers: raise ValueError("containers missing")
    for container in containers:
        image=container.get("image","")
        if not image or image.endswith(":latest"): raise ValueError("image must use an immutable tag or digest")
        if not container.get("resources",{}).get("requests"): raise ValueError("resource requests required")
    return True
