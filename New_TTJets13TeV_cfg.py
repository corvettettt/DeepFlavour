import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2016C/JetHT/MINIAOD/PromptReco-v2/000/276/064/00000/1257B839-9F40-E611-BF0E-02163E01393D.root',
'/store/mc/RunIISpring16MiniAODv2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/00000/321CA628-FF32-E611-994A-B083FED42FE4.root'] );

#readFiles.extend( [
#] );
secFiles.extend( [
               ] )
