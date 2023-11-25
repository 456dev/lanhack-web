{ mkElmDerivation }:

mkElmDerivation {
  pname = "frontend";
  version = "0.1.0";

  src = ./.;

  outputJavaScript = true;
  optimizationLevel = 2;
}