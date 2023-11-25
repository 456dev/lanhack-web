{
  inputs.mkElmDerivation.url = "github:jeslie0/mkElmDerivation";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { mkElmDerivation, nixpkgs, self }:
  let inherit (nixpkgs) legacyPackages lib;
  in {
    packages = lib.genAttrs lib.systems.flakeExposed (system:
    let pkgs = import nixpkgs { inherit system; overlays = [ mkElmDerivation.overlays.mkElmDerivation ]; };
    in rec {
      frontend = pkgs.callPackage ./frontend.nix { };
      backend = pkgs.python311Packages.callPackage ./backend.nix { };

      default = pkgs.linkFarm "lanhack-web" [
        {
          name = "frontend";
          path = frontend;
        }
        {
          name = "backend";
          path = backend;
        }
      ];
    });
  };
}