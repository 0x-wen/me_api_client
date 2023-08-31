# swagger_client.QueryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cosmos_auth_v1_beta1_account**](QueryApi.md#cosmos_auth_v1_beta1_account) | **GET** /cosmos/auth/v1beta1/accounts/{address} | Account returns account details based on address.
[**cosmos_auth_v1_beta1_account_address_by_id**](QueryApi.md#cosmos_auth_v1_beta1_account_address_by_id) | **GET** /cosmos/auth/v1beta1/address_by_id/{id} | AccountAddressByID returns account address based on account number.
[**cosmos_auth_v1_beta1_account_info**](QueryApi.md#cosmos_auth_v1_beta1_account_info) | **GET** /cosmos/auth/v1beta1/account_info/{address} | AccountInfo queries account info which is common to all account types.
[**cosmos_auth_v1_beta1_accounts**](QueryApi.md#cosmos_auth_v1_beta1_accounts) | **GET** /cosmos/auth/v1beta1/accounts | Accounts returns all the existing accounts.
[**cosmos_auth_v1_beta1_address_bytes_to_string**](QueryApi.md#cosmos_auth_v1_beta1_address_bytes_to_string) | **GET** /cosmos/auth/v1beta1/bech32/{address_bytes} | AddressBytesToString converts Account Address bytes to string
[**cosmos_auth_v1_beta1_address_string_to_bytes**](QueryApi.md#cosmos_auth_v1_beta1_address_string_to_bytes) | **GET** /cosmos/auth/v1beta1/bech32/{address_string} | AddressStringToBytes converts Address string to bytes
[**cosmos_auth_v1_beta1_bech32_prefix**](QueryApi.md#cosmos_auth_v1_beta1_bech32_prefix) | **GET** /cosmos/auth/v1beta1/bech32 | Bech32Prefix queries bech32Prefix
[**cosmos_auth_v1_beta1_module_account_by_name**](QueryApi.md#cosmos_auth_v1_beta1_module_account_by_name) | **GET** /cosmos/auth/v1beta1/module_accounts/{name} | ModuleAccountByName returns the module account info by module name
[**cosmos_auth_v1_beta1_module_accounts**](QueryApi.md#cosmos_auth_v1_beta1_module_accounts) | **GET** /cosmos/auth/v1beta1/module_accounts | ModuleAccounts returns all the existing module accounts.
[**cosmos_auth_v1_beta1_params**](QueryApi.md#cosmos_auth_v1_beta1_params) | **GET** /cosmos/auth/v1beta1/params | Params queries all parameters.
[**cosmos_authz_v1_beta1_grantee_grants**](QueryApi.md#cosmos_authz_v1_beta1_grantee_grants) | **GET** /cosmos/authz/v1beta1/grants/grantee/{grantee} | GranteeGrants returns a list of &#x60;GrantAuthorization&#x60; by grantee.
[**cosmos_authz_v1_beta1_granter_grants**](QueryApi.md#cosmos_authz_v1_beta1_granter_grants) | **GET** /cosmos/authz/v1beta1/grants/granter/{granter} | GranterGrants returns list of &#x60;GrantAuthorization&#x60;, granted by granter.
[**cosmos_authz_v1_beta1_grants**](QueryApi.md#cosmos_authz_v1_beta1_grants) | **GET** /cosmos/authz/v1beta1/grants | Returns list of &#x60;Authorization&#x60;, granted to the grantee by the granter.
[**cosmos_bank_v1_beta1_all_balances**](QueryApi.md#cosmos_bank_v1_beta1_all_balances) | **GET** /cosmos/bank/v1beta1/balances/{address} | AllBalances queries the balance of all coins for a single account.
[**cosmos_bank_v1_beta1_balance**](QueryApi.md#cosmos_bank_v1_beta1_balance) | **GET** /cosmos/bank/v1beta1/balances/{address}/by_denom | Balance queries the balance of a single coin for a single account.
[**cosmos_bank_v1_beta1_denom_metadata**](QueryApi.md#cosmos_bank_v1_beta1_denom_metadata) | **GET** /cosmos/bank/v1beta1/denoms_metadata/{denom} | DenomsMetadata queries the client metadata of a given coin denomination.
[**cosmos_bank_v1_beta1_denom_owners**](QueryApi.md#cosmos_bank_v1_beta1_denom_owners) | **GET** /cosmos/bank/v1beta1/denom_owners/{denom} | DenomOwners queries for all account addresses that own a particular token denomination.
[**cosmos_bank_v1_beta1_denoms_metadata**](QueryApi.md#cosmos_bank_v1_beta1_denoms_metadata) | **GET** /cosmos/bank/v1beta1/denoms_metadata | DenomsMetadata queries the client metadata for all registered coin denominations.
[**cosmos_bank_v1_beta1_params**](QueryApi.md#cosmos_bank_v1_beta1_params) | **GET** /cosmos/bank/v1beta1/params | Params queries the parameters of x/bank module.
[**cosmos_bank_v1_beta1_send_enabled**](QueryApi.md#cosmos_bank_v1_beta1_send_enabled) | **GET** /cosmos/bank/v1beta1/send_enabled | SendEnabled queries for SendEnabled entries.
[**cosmos_bank_v1_beta1_spendable_balance_by_denom**](QueryApi.md#cosmos_bank_v1_beta1_spendable_balance_by_denom) | **GET** /cosmos/bank/v1beta1/spendable_balances/{address}/by_denom | SpendableBalanceByDenom queries the spendable balance of a single denom for a single account.
[**cosmos_bank_v1_beta1_spendable_balances**](QueryApi.md#cosmos_bank_v1_beta1_spendable_balances) | **GET** /cosmos/bank/v1beta1/spendable_balances/{address} | SpendableBalances queries the spendable balance of all coins for a single account.
[**cosmos_bank_v1_beta1_supply_of**](QueryApi.md#cosmos_bank_v1_beta1_supply_of) | **GET** /cosmos/bank/v1beta1/supply/by_denom | SupplyOf queries the supply of a single coin.
[**cosmos_bank_v1_beta1_total_supply**](QueryApi.md#cosmos_bank_v1_beta1_total_supply) | **GET** /cosmos/bank/v1beta1/supply | TotalSupply queries the total supply of all coins.
[**cosmos_consensus_v1_params**](QueryApi.md#cosmos_consensus_v1_params) | **GET** /cosmos/consensus/v1/params | Params queries the parameters of x/consensus_param module.
[**cosmos_distribution_v1_beta1_delegation_rewards**](QueryApi.md#cosmos_distribution_v1_beta1_delegation_rewards) | **GET** /cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address} | DelegationRewards queries the total rewards accrued by a delegation.
[**cosmos_distribution_v1_beta1_params**](QueryApi.md#cosmos_distribution_v1_beta1_params) | **GET** /cosmos/distribution/v1beta1/params | Params queries params of the distribution module.
[**cosmos_distribution_v1_beta1_validator_distribution_info**](QueryApi.md#cosmos_distribution_v1_beta1_validator_distribution_info) | **GET** /cosmos/distribution/v1beta1/validators/{validator_address} | ValidatorDistributionInfo queries validator commission and self-delegation rewards for validator
[**cosmos_evidence_v1_beta1_all_evidence**](QueryApi.md#cosmos_evidence_v1_beta1_all_evidence) | **GET** /cosmos/evidence/v1beta1/evidence | AllEvidence queries all evidence.
[**cosmos_evidence_v1_beta1_evidence**](QueryApi.md#cosmos_evidence_v1_beta1_evidence) | **GET** /cosmos/evidence/v1beta1/evidence/{hash} | Evidence queries evidence based on evidence hash.
[**cosmos_feegrant_v1_beta1_allowance**](QueryApi.md#cosmos_feegrant_v1_beta1_allowance) | **GET** /cosmos/feegrant/v1beta1/allowance/{granter}/{grantee} | Allowance returns fee granted to the grantee by the granter.
[**cosmos_feegrant_v1_beta1_allowances**](QueryApi.md#cosmos_feegrant_v1_beta1_allowances) | **GET** /cosmos/feegrant/v1beta1/allowances/{grantee} | Allowances returns all the grants for address.
[**cosmos_feegrant_v1_beta1_allowances_by_granter**](QueryApi.md#cosmos_feegrant_v1_beta1_allowances_by_granter) | **GET** /cosmos/feegrant/v1beta1/issued/{granter} | AllowancesByGranter returns all the grants given by an address
[**cosmos_gov_v1_beta1_deposit**](QueryApi.md#cosmos_gov_v1_beta1_deposit) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor} | Deposit queries single deposit information based proposalID, depositAddr.
[**cosmos_gov_v1_beta1_deposits**](QueryApi.md#cosmos_gov_v1_beta1_deposits) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id}/deposits | Deposits queries all deposits of a single proposal.
[**cosmos_gov_v1_beta1_params**](QueryApi.md#cosmos_gov_v1_beta1_params) | **GET** /cosmos/gov/v1beta1/params/{params_type} | Params queries all parameters of the gov module.
[**cosmos_gov_v1_beta1_proposal**](QueryApi.md#cosmos_gov_v1_beta1_proposal) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id} | Proposal queries proposal details based on ProposalID.
[**cosmos_gov_v1_beta1_proposals**](QueryApi.md#cosmos_gov_v1_beta1_proposals) | **GET** /cosmos/gov/v1beta1/proposals | Proposals queries all proposals based on given status.
[**cosmos_gov_v1_beta1_tally_result**](QueryApi.md#cosmos_gov_v1_beta1_tally_result) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id}/tally | TallyResult queries the tally of a proposal vote.
[**cosmos_gov_v1_beta1_vote**](QueryApi.md#cosmos_gov_v1_beta1_vote) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter} | Vote queries voted information based on proposalID, voterAddr.
[**cosmos_gov_v1_beta1_votes**](QueryApi.md#cosmos_gov_v1_beta1_votes) | **GET** /cosmos/gov/v1beta1/proposals/{proposal_id}/votes | Votes queries votes of a given proposal.
[**cosmos_gov_v1_deposit**](QueryApi.md#cosmos_gov_v1_deposit) | **GET** /cosmos/gov/v1/proposals/{proposal_id}/deposits/{depositor} | Deposit queries single deposit information based proposalID, depositAddr.
[**cosmos_gov_v1_deposits**](QueryApi.md#cosmos_gov_v1_deposits) | **GET** /cosmos/gov/v1/proposals/{proposal_id}/deposits | Deposits queries all deposits of a single proposal.
[**cosmos_gov_v1_params**](QueryApi.md#cosmos_gov_v1_params) | **GET** /cosmos/gov/v1/params/{params_type} | Params queries all parameters of the gov module.
[**cosmos_gov_v1_proposal**](QueryApi.md#cosmos_gov_v1_proposal) | **GET** /cosmos/gov/v1/proposals/{proposal_id} | Proposal queries proposal details based on ProposalID.
[**cosmos_gov_v1_proposals**](QueryApi.md#cosmos_gov_v1_proposals) | **GET** /cosmos/gov/v1/proposals | Proposals queries all proposals based on given status.
[**cosmos_gov_v1_tally_result**](QueryApi.md#cosmos_gov_v1_tally_result) | **GET** /cosmos/gov/v1/proposals/{proposal_id}/tally | TallyResult queries the tally of a proposal vote.
[**cosmos_gov_v1_vote**](QueryApi.md#cosmos_gov_v1_vote) | **GET** /cosmos/gov/v1/proposals/{proposal_id}/votes/{voter} | Vote queries voted information based on proposalID, voterAddr.
[**cosmos_gov_v1_votes**](QueryApi.md#cosmos_gov_v1_votes) | **GET** /cosmos/gov/v1/proposals/{proposal_id}/votes | Votes queries votes of a given proposal.
[**cosmos_group_v1_group_info**](QueryApi.md#cosmos_group_v1_group_info) | **GET** /cosmos/group/v1/group_info/{group_id} | GroupInfo queries group info based on group id.
[**cosmos_group_v1_group_members**](QueryApi.md#cosmos_group_v1_group_members) | **GET** /cosmos/group/v1/group_members/{group_id} | GroupMembers queries members of a group by group id.
[**cosmos_group_v1_groups**](QueryApi.md#cosmos_group_v1_groups) | **GET** /cosmos/group/v1/groups | Groups queries all groups in state.
[**cosmos_group_v1_groups_by_admin**](QueryApi.md#cosmos_group_v1_groups_by_admin) | **GET** /cosmos/group/v1/groups_by_admin/{admin} | GroupsByAdmin queries groups by admin address.
[**cosmos_group_v1_groups_by_member**](QueryApi.md#cosmos_group_v1_groups_by_member) | **GET** /cosmos/group/v1/groups_by_member/{address} | GroupsByMember queries groups by member address.
[**cosmos_mint_v1_beta1_annual_provisions**](QueryApi.md#cosmos_mint_v1_beta1_annual_provisions) | **GET** /cosmos/mint/v1beta1/annual_provisions | AnnualProvisions current minting annual provisions value.
[**cosmos_mint_v1_beta1_inflation**](QueryApi.md#cosmos_mint_v1_beta1_inflation) | **GET** /cosmos/mint/v1beta1/inflation | Inflation returns the current minting inflation value.
[**cosmos_mint_v1_beta1_params**](QueryApi.md#cosmos_mint_v1_beta1_params) | **GET** /cosmos/mint/v1beta1/params | Params returns the total set of minting parameters.
[**cosmos_nft_v1_beta1_balance**](QueryApi.md#cosmos_nft_v1_beta1_balance) | **GET** /cosmos/nft/v1beta1/balance/{owner}/{class_id} | Balance queries the number of NFTs of a given class owned by the owner, same as balanceOf in ERC721
[**cosmos_nft_v1_beta1_class**](QueryApi.md#cosmos_nft_v1_beta1_class) | **GET** /cosmos/nft/v1beta1/classes/{class_id} | Class queries an NFT class based on its id
[**cosmos_nft_v1_beta1_classes**](QueryApi.md#cosmos_nft_v1_beta1_classes) | **GET** /cosmos/nft/v1beta1/classes | Classes queries all NFT classes
[**cosmos_nft_v1_beta1_nft**](QueryApi.md#cosmos_nft_v1_beta1_nft) | **GET** /cosmos/nft/v1beta1/nfts/{class_id}/{id} | NFT queries an NFT based on its class and id.
[**cosmos_nft_v1_beta1_nfts**](QueryApi.md#cosmos_nft_v1_beta1_nfts) | **GET** /cosmos/nft/v1beta1/nfts | NFTs queries all NFTs of a given class or owner,choose at least one of the two, similar to tokenByIndex in ERC721Enumerable
[**cosmos_nft_v1_beta1_owner**](QueryApi.md#cosmos_nft_v1_beta1_owner) | **GET** /cosmos/nft/v1beta1/owner/{class_id}/{id} | Owner queries the owner of the NFT based on its class and id, same as ownerOf in ERC721
[**cosmos_nft_v1_beta1_supply**](QueryApi.md#cosmos_nft_v1_beta1_supply) | **GET** /cosmos/nft/v1beta1/supply/{class_id} | Supply queries the number of NFTs from the given class, same as totalSupply of ERC721.
[**cosmos_params_v1_beta1_params**](QueryApi.md#cosmos_params_v1_beta1_params) | **GET** /cosmos/params/v1beta1/params | Params queries a specific parameter of a module, given its subspace and key.
[**cosmos_params_v1_beta1_subspaces**](QueryApi.md#cosmos_params_v1_beta1_subspaces) | **GET** /cosmos/params/v1beta1/subspaces | Subspaces queries for all registered subspaces and all keys for a subspace.
[**cosmos_slashing_v1_beta1_params**](QueryApi.md#cosmos_slashing_v1_beta1_params) | **GET** /cosmos/slashing/v1beta1/params | Params queries the parameters of slashing module
[**cosmos_slashing_v1_beta1_signing_info**](QueryApi.md#cosmos_slashing_v1_beta1_signing_info) | **GET** /cosmos/slashing/v1beta1/signing_infos/{cons_address} | SigningInfo queries the signing info of given cons address
[**cosmos_slashing_v1_beta1_signing_infos**](QueryApi.md#cosmos_slashing_v1_beta1_signing_infos) | **GET** /cosmos/slashing/v1beta1/signing_infos | SigningInfos queries signing info of all validators
[**cosmos_staking_v1_beta1_delegation**](QueryApi.md#cosmos_staking_v1_beta1_delegation) | **GET** /cosmos/staking/v1beta1/delegation/{delegator_addr} | Delegation queries delegate info for given validator delegator pair.
[**cosmos_staking_v1_beta1_fixed_deposit**](QueryApi.md#cosmos_staking_v1_beta1_fixed_deposit) | **GET** /cosmos/staking/v1beta1/fixed_deposit/{id} | Queries a list of FixedDeposit items.
[**cosmos_staking_v1_beta1_fixed_deposit_all**](QueryApi.md#cosmos_staking_v1_beta1_fixed_deposit_all) | **GET** /cosmos/staking/v1beta1/fixed_deposit | 
[**cosmos_staking_v1_beta1_fixed_deposit_by_acct**](QueryApi.md#cosmos_staking_v1_beta1_fixed_deposit_by_acct) | **GET** /cosmos/staking/v1beta1/fixed_deposit_by_acct/{account}/{query_type} | Queries a list of FixedDepositByAcct items.
[**cosmos_staking_v1_beta1_fixed_deposit_by_region**](QueryApi.md#cosmos_staking_v1_beta1_fixed_deposit_by_region) | **GET** /cosmos/staking/v1beta1/fixed_deposit_by_region/{regionid} | Queries a list of FixedDepositByRegion items.
[**cosmos_staking_v1_beta1_fixed_deposit_interest_rate**](QueryApi.md#cosmos_staking_v1_beta1_fixed_deposit_interest_rate) | **GET** /cosmos/staking/v1beta1/fixed_deposit_interest_rate | Queries FixedDepositInterest Item.
[**cosmos_staking_v1_beta1_historical_info**](QueryApi.md#cosmos_staking_v1_beta1_historical_info) | **GET** /cosmos/staking/v1beta1/historical_info/{height} | HistoricalInfo queries the historical info for given height.
[**cosmos_staking_v1_beta1_kyc**](QueryApi.md#cosmos_staking_v1_beta1_kyc) | **GET** /cosmos/staking/v1beta1/kyc/{account} | Queries a list of Kyc items.
[**cosmos_staking_v1_beta1_kyc_all**](QueryApi.md#cosmos_staking_v1_beta1_kyc_all) | **GET** /cosmos/staking/v1beta1/kyc | 
[**cosmos_staking_v1_beta1_kyc_by_region**](QueryApi.md#cosmos_staking_v1_beta1_kyc_by_region) | **GET** /cosmos/staking/v1beta1/kyc_by_region/{regionId} | Queries a list of KycByRegion items.
[**cosmos_staking_v1_beta1_params**](QueryApi.md#cosmos_staking_v1_beta1_params) | **GET** /cosmos/staking/v1beta1/params | Parameters queries the staking parameters.
[**cosmos_staking_v1_beta1_pool**](QueryApi.md#cosmos_staking_v1_beta1_pool) | **GET** /cosmos/staking/v1beta1/pool | Pool queries the pool info.
[**cosmos_staking_v1_beta1_region**](QueryApi.md#cosmos_staking_v1_beta1_region) | **GET** /cosmos/staking/v1beta1/region/{regionId} | Queries a list of Region items.
[**cosmos_staking_v1_beta1_region_all**](QueryApi.md#cosmos_staking_v1_beta1_region_all) | **GET** /cosmos/staking/v1beta1/region | 
[**cosmos_staking_v1_beta1_siid**](QueryApi.md#cosmos_staking_v1_beta1_siid) | **GET** /cosmos/staking/v1beta1/siid/{siid} | 
[**cosmos_staking_v1_beta1_siid_all**](QueryApi.md#cosmos_staking_v1_beta1_siid_all) | **GET** /cosmos/staking/v1beta1/siid | 
[**cosmos_staking_v1_beta1_siid_by_account**](QueryApi.md#cosmos_staking_v1_beta1_siid_by_account) | **GET** /cosmos/staking/v1beta1/siid_by_account/{account} | 
[**cosmos_staking_v1_beta1_unbonding_delegation**](QueryApi.md#cosmos_staking_v1_beta1_unbonding_delegation) | **GET** /cosmos/staking/v1beta1/unbonding_delegation/{delegator_addr} | UnbondingDelegation queries unbonding info for given validator delegator pair.
[**cosmos_staking_v1_beta1_validator**](QueryApi.md#cosmos_staking_v1_beta1_validator) | **GET** /cosmos/staking/v1beta1/validators/{validator_addr} | Validator queries validator info for given validator address.
[**cosmos_staking_v1_beta1_validator_delegations**](QueryApi.md#cosmos_staking_v1_beta1_validator_delegations) | **GET** /cosmos/staking/v1beta1/validators/{validator_addr}/delegations | ValidatorDelegations queries delegate info for given validator.
[**cosmos_staking_v1_beta1_validators**](QueryApi.md#cosmos_staking_v1_beta1_validators) | **GET** /cosmos/staking/v1beta1/validators | Validators queries all validators that match the given status.
[**cosmos_upgrade_v1_beta1_applied_plan**](QueryApi.md#cosmos_upgrade_v1_beta1_applied_plan) | **GET** /cosmos/upgrade/v1beta1/applied_plan/{name} | AppliedPlan queries a previously applied upgrade plan by its name.
[**cosmos_upgrade_v1_beta1_authority**](QueryApi.md#cosmos_upgrade_v1_beta1_authority) | **GET** /cosmos/upgrade/v1beta1/authority | Returns the account with authority to conduct upgrades
[**cosmos_upgrade_v1_beta1_current_plan**](QueryApi.md#cosmos_upgrade_v1_beta1_current_plan) | **GET** /cosmos/upgrade/v1beta1/current_plan | CurrentPlan queries the current upgrade plan.
[**cosmos_upgrade_v1_beta1_module_versions**](QueryApi.md#cosmos_upgrade_v1_beta1_module_versions) | **GET** /cosmos/upgrade/v1beta1/module_versions | ModuleVersions queries the list of module versions from state.
[**cosmos_upgrade_v1_beta1_upgraded_consensus_state**](QueryApi.md#cosmos_upgrade_v1_beta1_upgraded_consensus_state) | **GET** /cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height} | UpgradedConsensusState queries the consensus state that will serve as a trusted kernel for the next version of this chain. It will only be stored at the last height of this chain. UpgradedConsensusState RPC not supported with legacy querier This rpc is deprecated now that IBC has its own replacement (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)
[**cosmwasm_wasm_v1_all_contract_state**](QueryApi.md#cosmwasm_wasm_v1_all_contract_state) | **GET** /cosmwasm/wasm/v1/contract/{address}/state | AllContractState gets all raw store data for a single contract
[**cosmwasm_wasm_v1_code**](QueryApi.md#cosmwasm_wasm_v1_code) | **GET** /cosmwasm/wasm/v1/code/{code_id} | Code gets the binary code and metadata for a singe wasm code
[**cosmwasm_wasm_v1_codes**](QueryApi.md#cosmwasm_wasm_v1_codes) | **GET** /cosmwasm/wasm/v1/code | Codes gets the metadata for all stored wasm codes
[**cosmwasm_wasm_v1_contract_history**](QueryApi.md#cosmwasm_wasm_v1_contract_history) | **GET** /cosmwasm/wasm/v1/contract/{address}/history | ContractHistory gets the contract code history
[**cosmwasm_wasm_v1_contract_info**](QueryApi.md#cosmwasm_wasm_v1_contract_info) | **GET** /cosmwasm/wasm/v1/contract/{address} | ContractInfo gets the contract meta data
[**cosmwasm_wasm_v1_contracts_by_code**](QueryApi.md#cosmwasm_wasm_v1_contracts_by_code) | **GET** /cosmwasm/wasm/v1/code/{code_id}/contracts | ContractsByCode lists all smart contracts for a code id
[**cosmwasm_wasm_v1_contracts_by_creator**](QueryApi.md#cosmwasm_wasm_v1_contracts_by_creator) | **GET** /cosmwasm/wasm/v1/contracts/creator/{creator_address} | ContractsByCreator gets the contracts by creator
[**cosmwasm_wasm_v1_params**](QueryApi.md#cosmwasm_wasm_v1_params) | **GET** /cosmwasm/wasm/v1/codes/params | Params gets the module params
[**cosmwasm_wasm_v1_pinned_codes**](QueryApi.md#cosmwasm_wasm_v1_pinned_codes) | **GET** /cosmwasm/wasm/v1/codes/pinned | PinnedCodes gets the pinned code ids
[**cosmwasm_wasm_v1_raw_contract_state**](QueryApi.md#cosmwasm_wasm_v1_raw_contract_state) | **GET** /cosmwasm/wasm/v1/contract/{address}/raw/{query_data} | RawContractState gets single key from the raw store data of a contract
[**cosmwasm_wasm_v1_smart_contract_state**](QueryApi.md#cosmwasm_wasm_v1_smart_contract_state) | **GET** /cosmwasm/wasm/v1/contract/{address}/smart/{query_data} | SmartContractState get smart query result from the contract
[**ibc_applications_fee_v1_counterparty_payee**](QueryApi.md#ibc_applications_fee_v1_counterparty_payee) | **GET** /ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/counterparty_payee | CounterpartyPayee returns the registered counterparty payee for forward relaying
[**ibc_applications_fee_v1_fee_enabled_channel**](QueryApi.md#ibc_applications_fee_v1_fee_enabled_channel) | **GET** /ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/fee_enabled | FeeEnabledChannel returns true if the provided port and channel identifiers belong to a fee enabled channel
[**ibc_applications_fee_v1_fee_enabled_channels**](QueryApi.md#ibc_applications_fee_v1_fee_enabled_channels) | **GET** /ibc/apps/fee/v1/fee_enabled | FeeEnabledChannels returns a list of all fee enabled channels
[**ibc_applications_fee_v1_incentivized_packet**](QueryApi.md#ibc_applications_fee_v1_incentivized_packet) | **GET** /ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/incentivized_packet | IncentivizedPacket returns all packet fees for a packet given its identifier
[**ibc_applications_fee_v1_incentivized_packets**](QueryApi.md#ibc_applications_fee_v1_incentivized_packets) | **GET** /ibc/apps/fee/v1/incentivized_packets | IncentivizedPackets returns all incentivized packets and their associated fees
[**ibc_applications_fee_v1_incentivized_packets_for_channel**](QueryApi.md#ibc_applications_fee_v1_incentivized_packets_for_channel) | **GET** /ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/incentivized_packets | Gets all incentivized packets for a specific channel
[**ibc_applications_fee_v1_payee**](QueryApi.md#ibc_applications_fee_v1_payee) | **GET** /ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/payee | Payee returns the registered payee address for a specific channel given the relayer address
[**ibc_applications_fee_v1_total_ack_fees**](QueryApi.md#ibc_applications_fee_v1_total_ack_fees) | **GET** /ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_ack_fees | TotalAckFees returns the total acknowledgement fees for a packet given its identifier
[**ibc_applications_fee_v1_total_recv_fees**](QueryApi.md#ibc_applications_fee_v1_total_recv_fees) | **GET** /ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_recv_fees | TotalRecvFees returns the total receive fees for a packet given its identifier
[**ibc_applications_fee_v1_total_timeout_fees**](QueryApi.md#ibc_applications_fee_v1_total_timeout_fees) | **GET** /ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_timeout_fees | TotalTimeoutFees returns the total timeout fees for a packet given its identifier
[**ibc_applications_interchain_accounts_controller_v1_interchain_account**](QueryApi.md#ibc_applications_interchain_accounts_controller_v1_interchain_account) | **GET** /ibc/apps/interchain_accounts/controller/v1/owners/{owner}/connections/{connection_id} | InterchainAccount returns the interchain account address for a given owner address on a given connection
[**ibc_applications_interchain_accounts_controller_v1_params**](QueryApi.md#ibc_applications_interchain_accounts_controller_v1_params) | **GET** /ibc/apps/interchain_accounts/controller/v1/params | Params queries all parameters of the ICA controller submodule.
[**ibc_applications_interchain_accounts_host_v1_params**](QueryApi.md#ibc_applications_interchain_accounts_host_v1_params) | **GET** /ibc/apps/interchain_accounts/host/v1/params | Params queries all parameters of the ICA host submodule.
[**ibc_applications_transfer_v1_denom_hash**](QueryApi.md#ibc_applications_transfer_v1_denom_hash) | **GET** /ibc/apps/transfer/v1/denom_hashes/{trace} | DenomHash queries a denomination hash information.
[**ibc_applications_transfer_v1_denom_trace**](QueryApi.md#ibc_applications_transfer_v1_denom_trace) | **GET** /ibc/apps/transfer/v1/denom_traces/{hash} | DenomTrace queries a denomination trace information.
[**ibc_applications_transfer_v1_denom_traces**](QueryApi.md#ibc_applications_transfer_v1_denom_traces) | **GET** /ibc/apps/transfer/v1/denom_traces | DenomTraces queries all denomination traces.
[**ibc_applications_transfer_v1_escrow_address**](QueryApi.md#ibc_applications_transfer_v1_escrow_address) | **GET** /ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_address | EscrowAddress returns the escrow address for a particular port and channel id.
[**ibc_applications_transfer_v1_params**](QueryApi.md#ibc_applications_transfer_v1_params) | **GET** /ibc/apps/transfer/v1/params | Params queries all parameters of the ibc-transfer module.
[**ibc_applications_transfer_v1_total_escrow_for_denom**](QueryApi.md#ibc_applications_transfer_v1_total_escrow_for_denom) | **GET** /ibc/apps/transfer/v1/denoms/{denom}/total_escrow | TotalEscrowForDenom returns the total amount of tokens in escrow based on the denom.
[**ibc_core_channel_v1_channel**](QueryApi.md#ibc_core_channel_v1_channel) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id} | Channel queries an IBC Channel.
[**ibc_core_channel_v1_channel_client_state**](QueryApi.md#ibc_core_channel_v1_channel_client_state) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state | ChannelClientState queries for the client state for the channel associated with the provided channel identifiers.
[**ibc_core_channel_v1_channel_consensus_state**](QueryApi.md#ibc_core_channel_v1_channel_consensus_state) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height} | ChannelConsensusState queries for the consensus state for the channel associated with the provided channel identifiers.
[**ibc_core_channel_v1_channels**](QueryApi.md#ibc_core_channel_v1_channels) | **GET** /ibc/core/channel/v1/channels | Channels queries all the IBC channels of a chain.
[**ibc_core_channel_v1_connection_channels**](QueryApi.md#ibc_core_channel_v1_connection_channels) | **GET** /ibc/core/channel/v1/connections/{connection}/channels | ConnectionChannels queries all the channels associated with a connection end.
[**ibc_core_channel_v1_next_sequence_receive**](QueryApi.md#ibc_core_channel_v1_next_sequence_receive) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence | NextSequenceReceive returns the next receive sequence for a given channel.
[**ibc_core_channel_v1_packet_acknowledgement**](QueryApi.md#ibc_core_channel_v1_packet_acknowledgement) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence} | PacketAcknowledgement queries a stored packet acknowledgement hash.
[**ibc_core_channel_v1_packet_acknowledgements**](QueryApi.md#ibc_core_channel_v1_packet_acknowledgements) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements | PacketAcknowledgements returns all the packet acknowledgements associated with a channel.
[**ibc_core_channel_v1_packet_commitment**](QueryApi.md#ibc_core_channel_v1_packet_commitment) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence} | PacketCommitment queries a stored packet commitment hash.
[**ibc_core_channel_v1_packet_commitments**](QueryApi.md#ibc_core_channel_v1_packet_commitments) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments | PacketCommitments returns all the packet commitments hashes associated with a channel.
[**ibc_core_channel_v1_packet_receipt**](QueryApi.md#ibc_core_channel_v1_packet_receipt) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence} | PacketReceipt queries if a given packet sequence has been received on the queried chain
[**ibc_core_channel_v1_unreceived_acks**](QueryApi.md#ibc_core_channel_v1_unreceived_acks) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks | UnreceivedAcks returns all the unreceived IBC acknowledgements associated with a channel and sequences.
[**ibc_core_channel_v1_unreceived_packets**](QueryApi.md#ibc_core_channel_v1_unreceived_packets) | **GET** /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets | UnreceivedPackets returns all the unreceived IBC packets associated with a channel and sequences.
[**ibc_core_client_v1_client_params**](QueryApi.md#ibc_core_client_v1_client_params) | **GET** /ibc/core/client/v1/params | ClientParams queries all parameters of the ibc client submodule.
[**ibc_core_client_v1_client_state**](QueryApi.md#ibc_core_client_v1_client_state) | **GET** /ibc/core/client/v1/client_states/{client_id} | ClientState queries an IBC light client.
[**ibc_core_client_v1_client_states**](QueryApi.md#ibc_core_client_v1_client_states) | **GET** /ibc/core/client/v1/client_states | ClientStates queries all the IBC light clients of a chain.
[**ibc_core_client_v1_client_status**](QueryApi.md#ibc_core_client_v1_client_status) | **GET** /ibc/core/client/v1/client_status/{client_id} | Status queries the status of an IBC client.
[**ibc_core_client_v1_consensus_state**](QueryApi.md#ibc_core_client_v1_consensus_state) | **GET** /ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height} | ConsensusState queries a consensus state associated with a client state at a given height.
[**ibc_core_client_v1_consensus_state_heights**](QueryApi.md#ibc_core_client_v1_consensus_state_heights) | **GET** /ibc/core/client/v1/consensus_states/{client_id}/heights | ConsensusStateHeights queries the height of every consensus states associated with a given client.
[**ibc_core_client_v1_consensus_states**](QueryApi.md#ibc_core_client_v1_consensus_states) | **GET** /ibc/core/client/v1/consensus_states/{client_id} | ConsensusStates queries all the consensus state associated with a given client.
[**ibc_core_client_v1_upgraded_client_state**](QueryApi.md#ibc_core_client_v1_upgraded_client_state) | **GET** /ibc/core/client/v1/upgraded_client_states | UpgradedClientState queries an Upgraded IBC light client.
[**ibc_core_client_v1_upgraded_consensus_state**](QueryApi.md#ibc_core_client_v1_upgraded_consensus_state) | **GET** /ibc/core/client/v1/upgraded_consensus_states | UpgradedConsensusState queries an Upgraded IBC consensus state.
[**ibc_core_connection_v1_client_connections**](QueryApi.md#ibc_core_connection_v1_client_connections) | **GET** /ibc/core/connection/v1/client_connections/{client_id} | ClientConnections queries the connection paths associated with a client state.
[**ibc_core_connection_v1_connection**](QueryApi.md#ibc_core_connection_v1_connection) | **GET** /ibc/core/connection/v1/connections/{connection_id} | Connection queries an IBC connection end.
[**ibc_core_connection_v1_connection_client_state**](QueryApi.md#ibc_core_connection_v1_connection_client_state) | **GET** /ibc/core/connection/v1/connections/{connection_id}/client_state | ConnectionClientState queries the client state associated with the connection.
[**ibc_core_connection_v1_connection_consensus_state**](QueryApi.md#ibc_core_connection_v1_connection_consensus_state) | **GET** /ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height} | ConnectionConsensusState queries the consensus state associated with the connection.
[**ibc_core_connection_v1_connection_params**](QueryApi.md#ibc_core_connection_v1_connection_params) | **GET** /ibc/core/connection/v1/params | ConnectionParams queries all parameters of the ibc connection submodule.
[**ibc_core_connection_v1_connections**](QueryApi.md#ibc_core_connection_v1_connections) | **GET** /ibc/core/connection/v1/connections | Connections queries all the IBC connections of a chain.

# **cosmos_auth_v1_beta1_account**
> InlineResponse2002 cosmos_auth_v1_beta1_account(address)

Account returns account details based on address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address defines the address to query for.

try:
    # Account returns account details based on address.
    api_response = api_instance.cosmos_auth_v1_beta1_account(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address defines the address to query for. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_account_address_by_id**
> QueryAccountAddressByIDResponseIsTheResponseTypeForAccountAddressByIDRpcMethod cosmos_auth_v1_beta1_account_address_by_id(id, account_id=account_id)

AccountAddressByID returns account address based on account number.

Since: cosmos-sdk 0.46.2

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
id = 'id_example' # str | Deprecated, use account_id instead  id is the account number of the address to be queried. This field should have been an uint64 (like all account numbers), and will be updated to uint64 in a future version of the auth query.
account_id = 'account_id_example' # str | account_id is the account number of the address to be queried.  Since: cosmos-sdk 0.47 (optional)

try:
    # AccountAddressByID returns account address based on account number.
    api_response = api_instance.cosmos_auth_v1_beta1_account_address_by_id(id, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_account_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Deprecated, use account_id instead  id is the account number of the address to be queried. This field should have been an uint64 (like all account numbers), and will be updated to uint64 in a future version of the auth query. | 
 **account_id** | **str**| account_id is the account number of the address to be queried.  Since: cosmos-sdk 0.47 | [optional] 

### Return type

[**QueryAccountAddressByIDResponseIsTheResponseTypeForAccountAddressByIDRpcMethod**](QueryAccountAddressByIDResponseIsTheResponseTypeForAccountAddressByIDRpcMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_account_info**
> InlineResponse200 cosmos_auth_v1_beta1_account_info(address)

AccountInfo queries account info which is common to all account types.

Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the account address string.

try:
    # AccountInfo queries account info which is common to all account types.
    api_response = api_instance.cosmos_auth_v1_beta1_account_info(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the account address string. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_accounts**
> InlineResponse2001 cosmos_auth_v1_beta1_accounts(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Accounts returns all the existing accounts.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.  Since: cosmos-sdk 0.43

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Accounts returns all the existing accounts.
    api_response = api_instance.cosmos_auth_v1_beta1_accounts(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_address_bytes_to_string**
> InlineResponse2004 cosmos_auth_v1_beta1_address_bytes_to_string(address_bytes)

AddressBytesToString converts Account Address bytes to string

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address_bytes = 'B' # str | 

try:
    # AddressBytesToString converts Account Address bytes to string
    api_response = api_instance.cosmos_auth_v1_beta1_address_bytes_to_string(address_bytes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_address_bytes_to_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_bytes** | **str**|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_address_string_to_bytes**
> InlineResponse2005 cosmos_auth_v1_beta1_address_string_to_bytes(address_string)

AddressStringToBytes converts Address string to bytes

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address_string = 'address_string_example' # str | 

try:
    # AddressStringToBytes converts Address string to bytes
    api_response = api_instance.cosmos_auth_v1_beta1_address_string_to_bytes(address_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_address_string_to_bytes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_string** | **str**|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_bech32_prefix**
> InlineResponse2003 cosmos_auth_v1_beta1_bech32_prefix()

Bech32Prefix queries bech32Prefix

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Bech32Prefix queries bech32Prefix
    api_response = api_instance.cosmos_auth_v1_beta1_bech32_prefix()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_bech32_prefix: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_module_account_by_name**
> InlineResponse2007 cosmos_auth_v1_beta1_module_account_by_name(name)

ModuleAccountByName returns the module account info by module name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
name = 'name_example' # str | 

try:
    # ModuleAccountByName returns the module account info by module name
    api_response = api_instance.cosmos_auth_v1_beta1_module_account_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_module_account_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_module_accounts**
> InlineResponse2006 cosmos_auth_v1_beta1_module_accounts()

ModuleAccounts returns all the existing module accounts.

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # ModuleAccounts returns all the existing module accounts.
    api_response = api_instance.cosmos_auth_v1_beta1_module_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_module_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_auth_v1_beta1_params**
> InlineResponse2008 cosmos_auth_v1_beta1_params()

Params queries all parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries all parameters.
    api_response = api_instance.cosmos_auth_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_auth_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_authz_v1_beta1_grantee_grants**
> InlineResponse20010 cosmos_authz_v1_beta1_grantee_grants(grantee, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GranteeGrants returns a list of `GrantAuthorization` by grantee.

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
grantee = 'grantee_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GranteeGrants returns a list of `GrantAuthorization` by grantee.
    api_response = api_instance.cosmos_authz_v1_beta1_grantee_grants(grantee, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_authz_v1_beta1_grantee_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grantee** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_authz_v1_beta1_granter_grants**
> InlineResponse20011 cosmos_authz_v1_beta1_granter_grants(granter, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GranterGrants returns list of `GrantAuthorization`, granted by granter.

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
granter = 'granter_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GranterGrants returns list of `GrantAuthorization`, granted by granter.
    api_response = api_instance.cosmos_authz_v1_beta1_granter_grants(granter, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_authz_v1_beta1_granter_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granter** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_authz_v1_beta1_grants**
> InlineResponse2009 cosmos_authz_v1_beta1_grants(granter=granter, grantee=grantee, msg_type_url=msg_type_url, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Returns list of `Authorization`, granted to the grantee by the granter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
granter = 'granter_example' # str |  (optional)
grantee = 'grantee_example' # str |  (optional)
msg_type_url = 'msg_type_url_example' # str | Optional, msg_type_url, when set, will query only grants matching given msg type. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Returns list of `Authorization`, granted to the grantee by the granter.
    api_response = api_instance.cosmos_authz_v1_beta1_grants(granter=granter, grantee=grantee, msg_type_url=msg_type_url, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_authz_v1_beta1_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granter** | **str**|  | [optional] 
 **grantee** | **str**|  | [optional] 
 **msg_type_url** | **str**| Optional, msg_type_url, when set, will query only grants matching given msg type. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_all_balances**
> InlineResponse20012 cosmos_bank_v1_beta1_all_balances(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

AllBalances queries the balance of all coins for a single account.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address to query balances for.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # AllBalances queries the balance of all coins for a single account.
    api_response = api_instance.cosmos_bank_v1_beta1_all_balances(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_all_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address to query balances for. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_balance**
> InlineResponse20013 cosmos_bank_v1_beta1_balance(address, denom=denom)

Balance queries the balance of a single coin for a single account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address to query balances for.
denom = 'denom_example' # str | denom is the coin denom to query balances for. (optional)

try:
    # Balance queries the balance of a single coin for a single account.
    api_response = api_instance.cosmos_bank_v1_beta1_balance(address, denom=denom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address to query balances for. | 
 **denom** | **str**| denom is the coin denom to query balances for. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_denom_metadata**
> InlineResponse20016 cosmos_bank_v1_beta1_denom_metadata(denom)

DenomsMetadata queries the client metadata of a given coin denomination.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
denom = 'denom_example' # str | denom is the coin denom to query the metadata for.

try:
    # DenomsMetadata queries the client metadata of a given coin denomination.
    api_response = api_instance.cosmos_bank_v1_beta1_denom_metadata(denom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_denom_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denom** | **str**| denom is the coin denom to query the metadata for. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_denom_owners**
> InlineResponse20014 cosmos_bank_v1_beta1_denom_owners(denom, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

DenomOwners queries for all account addresses that own a particular token denomination.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.  Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
denom = 'denom_example' # str | denom defines the coin denomination to query all account holders for.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # DenomOwners queries for all account addresses that own a particular token denomination.
    api_response = api_instance.cosmos_bank_v1_beta1_denom_owners(denom, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_denom_owners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denom** | **str**| denom defines the coin denomination to query all account holders for. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_denoms_metadata**
> InlineResponse20015 cosmos_bank_v1_beta1_denoms_metadata(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

DenomsMetadata queries the client metadata for all registered coin denominations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # DenomsMetadata queries the client metadata for all registered coin denominations.
    api_response = api_instance.cosmos_bank_v1_beta1_denoms_metadata(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_denoms_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_params**
> InlineResponse20017 cosmos_bank_v1_beta1_params()

Params queries the parameters of x/bank module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries the parameters of x/bank module.
    api_response = api_instance.cosmos_bank_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_send_enabled**
> InlineResponse20018 cosmos_bank_v1_beta1_send_enabled(denoms=denoms, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

SendEnabled queries for SendEnabled entries.

This query only returns denominations that have specific SendEnabled settings. Any denomination that does not have a specific setting will use the default params.default_send_enabled, and will not be returned by this query.  Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
denoms = ['denoms_example'] # list[str] | denoms is the specific denoms you want look up. Leave empty to get all entries. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # SendEnabled queries for SendEnabled entries.
    api_response = api_instance.cosmos_bank_v1_beta1_send_enabled(denoms=denoms, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_send_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denoms** | [**list[str]**](str.md)| denoms is the specific denoms you want look up. Leave empty to get all entries. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_spendable_balance_by_denom**
> InlineResponse20020 cosmos_bank_v1_beta1_spendable_balance_by_denom(address, denom=denom)

SpendableBalanceByDenom queries the spendable balance of a single denom for a single account.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.  Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address to query balances for.
denom = 'denom_example' # str | denom is the coin denom to query balances for. (optional)

try:
    # SpendableBalanceByDenom queries the spendable balance of a single denom for a single account.
    api_response = api_instance.cosmos_bank_v1_beta1_spendable_balance_by_denom(address, denom=denom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_spendable_balance_by_denom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address to query balances for. | 
 **denom** | **str**| denom is the coin denom to query balances for. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_spendable_balances**
> InlineResponse20019 cosmos_bank_v1_beta1_spendable_balances(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

SpendableBalances queries the spendable balance of all coins for a single account.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.  Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address to query spendable balances for.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # SpendableBalances queries the spendable balance of all coins for a single account.
    api_response = api_instance.cosmos_bank_v1_beta1_spendable_balances(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_spendable_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address to query spendable balances for. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_supply_of**
> InlineResponse20021 cosmos_bank_v1_beta1_supply_of(denom=denom)

SupplyOf queries the supply of a single coin.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
denom = 'denom_example' # str | denom is the coin denom to query balances for. (optional)

try:
    # SupplyOf queries the supply of a single coin.
    api_response = api_instance.cosmos_bank_v1_beta1_supply_of(denom=denom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_supply_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denom** | **str**| denom is the coin denom to query balances for. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_bank_v1_beta1_total_supply**
> QueryTotalSupplyResponseIsTheResponseTypeForTheQueryTotalSupplyRPCmethod cosmos_bank_v1_beta1_total_supply(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

TotalSupply queries the total supply of all coins.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # TotalSupply queries the total supply of all coins.
    api_response = api_instance.cosmos_bank_v1_beta1_total_supply(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_bank_v1_beta1_total_supply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryTotalSupplyResponseIsTheResponseTypeForTheQueryTotalSupplyRPCmethod**](QueryTotalSupplyResponseIsTheResponseTypeForTheQueryTotalSupplyRPCmethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_consensus_v1_params**
> InlineResponse20030 cosmos_consensus_v1_params()

Params queries the parameters of x/consensus_param module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries the parameters of x/consensus_param module.
    api_response = api_instance.cosmos_consensus_v1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_consensus_v1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_distribution_v1_beta1_delegation_rewards**
> InlineResponse20031 cosmos_distribution_v1_beta1_delegation_rewards(delegator_address, validator_address)

DelegationRewards queries the total rewards accrued by a delegation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
delegator_address = 'delegator_address_example' # str | delegator_address defines the delegator address to query for.
validator_address = 'validator_address_example' # str | validator_address defines the validator address to query for.

try:
    # DelegationRewards queries the total rewards accrued by a delegation.
    api_response = api_instance.cosmos_distribution_v1_beta1_delegation_rewards(delegator_address, validator_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_distribution_v1_beta1_delegation_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_address** | **str**| delegator_address defines the delegator address to query for. | 
 **validator_address** | **str**| validator_address defines the validator address to query for. | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_distribution_v1_beta1_params**
> InlineResponse20032 cosmos_distribution_v1_beta1_params()

Params queries params of the distribution module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries params of the distribution module.
    api_response = api_instance.cosmos_distribution_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_distribution_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_distribution_v1_beta1_validator_distribution_info**
> InlineResponse20033 cosmos_distribution_v1_beta1_validator_distribution_info(validator_address)

ValidatorDistributionInfo queries validator commission and self-delegation rewards for validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
validator_address = 'validator_address_example' # str | validator_address defines the validator address to query for.

try:
    # ValidatorDistributionInfo queries validator commission and self-delegation rewards for validator
    api_response = api_instance.cosmos_distribution_v1_beta1_validator_distribution_info(validator_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_distribution_v1_beta1_validator_distribution_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_address** | **str**| validator_address defines the validator address to query for. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_evidence_v1_beta1_all_evidence**
> InlineResponse20034 cosmos_evidence_v1_beta1_all_evidence(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

AllEvidence queries all evidence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # AllEvidence queries all evidence.
    api_response = api_instance.cosmos_evidence_v1_beta1_all_evidence(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_evidence_v1_beta1_all_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_evidence_v1_beta1_evidence**
> InlineResponse20035 cosmos_evidence_v1_beta1_evidence(hash, evidence_hash=evidence_hash)

Evidence queries evidence based on evidence hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
hash = 'hash_example' # str | hash defines the evidence hash of the requested evidence.  Since: cosmos-sdk 0.47
evidence_hash = 'B' # str | evidence_hash defines the hash of the requested evidence. Deprecated: Use hash, a HEX encoded string, instead. (optional)

try:
    # Evidence queries evidence based on evidence hash.
    api_response = api_instance.cosmos_evidence_v1_beta1_evidence(hash, evidence_hash=evidence_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_evidence_v1_beta1_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| hash defines the evidence hash of the requested evidence.  Since: cosmos-sdk 0.47 | 
 **evidence_hash** | **str**| evidence_hash defines the hash of the requested evidence. Deprecated: Use hash, a HEX encoded string, instead. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_feegrant_v1_beta1_allowance**
> InlineResponse20036 cosmos_feegrant_v1_beta1_allowance(granter, grantee)

Allowance returns fee granted to the grantee by the granter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
granter = 'granter_example' # str | granter is the address of the user granting an allowance of their funds.
grantee = 'grantee_example' # str | grantee is the address of the user being granted an allowance of another user's funds.

try:
    # Allowance returns fee granted to the grantee by the granter.
    api_response = api_instance.cosmos_feegrant_v1_beta1_allowance(granter, grantee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_feegrant_v1_beta1_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granter** | **str**| granter is the address of the user granting an allowance of their funds. | 
 **grantee** | **str**| grantee is the address of the user being granted an allowance of another user&#x27;s funds. | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_feegrant_v1_beta1_allowances**
> InlineResponse20037 cosmos_feegrant_v1_beta1_allowances(grantee, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Allowances returns all the grants for address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
grantee = 'grantee_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Allowances returns all the grants for address.
    api_response = api_instance.cosmos_feegrant_v1_beta1_allowances(grantee, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_feegrant_v1_beta1_allowances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grantee** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_feegrant_v1_beta1_allowances_by_granter**
> InlineResponse20038 cosmos_feegrant_v1_beta1_allowances_by_granter(granter, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

AllowancesByGranter returns all the grants given by an address

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
granter = 'granter_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # AllowancesByGranter returns all the grants given by an address
    api_response = api_instance.cosmos_feegrant_v1_beta1_allowances_by_granter(granter, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_feegrant_v1_beta1_allowances_by_granter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granter** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_deposit**
> InlineResponse20043 cosmos_gov_v1_beta1_deposit(proposal_id, depositor)

Deposit queries single deposit information based proposalID, depositAddr.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
depositor = 'depositor_example' # str | depositor defines the deposit addresses from the proposals.

try:
    # Deposit queries single deposit information based proposalID, depositAddr.
    api_response = api_instance.cosmos_gov_v1_beta1_deposit(proposal_id, depositor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **depositor** | **str**| depositor defines the deposit addresses from the proposals. | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_deposits**
> InlineResponse20042 cosmos_gov_v1_beta1_deposits(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Deposits queries all deposits of a single proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Deposits queries all deposits of a single proposal.
    api_response = api_instance.cosmos_gov_v1_beta1_deposits(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_deposits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_params**
> InlineResponse20047 cosmos_gov_v1_beta1_params(params_type)

Params queries all parameters of the gov module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
params_type = 'params_type_example' # str | params_type defines which parameters to query for, can be one of \"voting\", \"tallying\" or \"deposit\".

try:
    # Params queries all parameters of the gov module.
    api_response = api_instance.cosmos_gov_v1_beta1_params(params_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params_type** | **str**| params_type defines which parameters to query for, can be one of \&quot;voting\&quot;, \&quot;tallying\&quot; or \&quot;deposit\&quot;. | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_proposal**
> InlineResponse20049 cosmos_gov_v1_beta1_proposal(proposal_id)

Proposal queries proposal details based on ProposalID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.

try:
    # Proposal queries proposal details based on ProposalID.
    api_response = api_instance.cosmos_gov_v1_beta1_proposal(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_proposals**
> InlineResponse20048 cosmos_gov_v1_beta1_proposals(proposal_status=proposal_status, voter=voter, depositor=depositor, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Proposals queries all proposals based on given status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_status = 'PROPOSAL_STATUS_UNSPECIFIED' # str | proposal_status defines the status of the proposals.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed. (optional) (default to PROPOSAL_STATUS_UNSPECIFIED)
voter = 'voter_example' # str | voter defines the voter address for the proposals. (optional)
depositor = 'depositor_example' # str | depositor defines the deposit addresses from the proposals. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Proposals queries all proposals based on given status.
    api_response = api_instance.cosmos_gov_v1_beta1_proposals(proposal_status=proposal_status, voter=voter, depositor=depositor, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_status** | **str**| proposal_status defines the status of the proposals.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed. | [optional] [default to PROPOSAL_STATUS_UNSPECIFIED]
 **voter** | **str**| voter defines the voter address for the proposals. | [optional] 
 **depositor** | **str**| depositor defines the deposit addresses from the proposals. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_tally_result**
> InlineResponse20050 cosmos_gov_v1_beta1_tally_result(proposal_id)

TallyResult queries the tally of a proposal vote.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.

try:
    # TallyResult queries the tally of a proposal vote.
    api_response = api_instance.cosmos_gov_v1_beta1_tally_result(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_tally_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_vote**
> InlineResponse20052 cosmos_gov_v1_beta1_vote(proposal_id, voter)

Vote queries voted information based on proposalID, voterAddr.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
voter = 'voter_example' # str | voter defines the voter address for the proposals.

try:
    # Vote queries voted information based on proposalID, voterAddr.
    api_response = api_instance.cosmos_gov_v1_beta1_vote(proposal_id, voter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **voter** | **str**| voter defines the voter address for the proposals. | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_beta1_votes**
> InlineResponse20051 cosmos_gov_v1_beta1_votes(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Votes queries votes of a given proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Votes queries votes of a given proposal.
    api_response = api_instance.cosmos_gov_v1_beta1_votes(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_beta1_votes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_deposit**
> InlineResponse20043 cosmos_gov_v1_deposit(proposal_id, depositor)

Deposit queries single deposit information based proposalID, depositAddr.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
depositor = 'depositor_example' # str | depositor defines the deposit addresses from the proposals.

try:
    # Deposit queries single deposit information based proposalID, depositAddr.
    api_response = api_instance.cosmos_gov_v1_deposit(proposal_id, depositor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **depositor** | **str**| depositor defines the deposit addresses from the proposals. | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_deposits**
> InlineResponse20042 cosmos_gov_v1_deposits(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Deposits queries all deposits of a single proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Deposits queries all deposits of a single proposal.
    api_response = api_instance.cosmos_gov_v1_deposits(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_deposits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_params**
> InlineResponse20039 cosmos_gov_v1_params(params_type)

Params queries all parameters of the gov module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
params_type = 'params_type_example' # str | params_type defines which parameters to query for, can be one of \"voting\", \"tallying\" or \"deposit\".

try:
    # Params queries all parameters of the gov module.
    api_response = api_instance.cosmos_gov_v1_params(params_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params_type** | **str**| params_type defines which parameters to query for, can be one of \&quot;voting\&quot;, \&quot;tallying\&quot; or \&quot;deposit\&quot;. | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_proposal**
> InlineResponse20041 cosmos_gov_v1_proposal(proposal_id)

Proposal queries proposal details based on ProposalID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.

try:
    # Proposal queries proposal details based on ProposalID.
    api_response = api_instance.cosmos_gov_v1_proposal(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_proposals**
> InlineResponse20040 cosmos_gov_v1_proposals(proposal_status=proposal_status, voter=voter, depositor=depositor, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Proposals queries all proposals based on given status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_status = 'PROPOSAL_STATUS_UNSPECIFIED' # str | proposal_status defines the status of the proposals.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed. (optional) (default to PROPOSAL_STATUS_UNSPECIFIED)
voter = 'voter_example' # str | voter defines the voter address for the proposals. (optional)
depositor = 'depositor_example' # str | depositor defines the deposit addresses from the proposals. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Proposals queries all proposals based on given status.
    api_response = api_instance.cosmos_gov_v1_proposals(proposal_status=proposal_status, voter=voter, depositor=depositor, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_status** | **str**| proposal_status defines the status of the proposals.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed. | [optional] [default to PROPOSAL_STATUS_UNSPECIFIED]
 **voter** | **str**| voter defines the voter address for the proposals. | [optional] 
 **depositor** | **str**| depositor defines the deposit addresses from the proposals. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_tally_result**
> InlineResponse20044 cosmos_gov_v1_tally_result(proposal_id)

TallyResult queries the tally of a proposal vote.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.

try:
    # TallyResult queries the tally of a proposal vote.
    api_response = api_instance.cosmos_gov_v1_tally_result(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_tally_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_vote**
> InlineResponse20046 cosmos_gov_v1_vote(proposal_id, voter)

Vote queries voted information based on proposalID, voterAddr.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
voter = 'voter_example' # str | voter defines the voter address for the proposals.

try:
    # Vote queries voted information based on proposalID, voterAddr.
    api_response = api_instance.cosmos_gov_v1_vote(proposal_id, voter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **voter** | **str**| voter defines the voter address for the proposals. | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_gov_v1_votes**
> InlineResponse20045 cosmos_gov_v1_votes(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Votes queries votes of a given proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
proposal_id = 'proposal_id_example' # str | proposal_id defines the unique id of the proposal.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Votes queries votes of a given proposal.
    api_response = api_instance.cosmos_gov_v1_votes(proposal_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_gov_v1_votes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal_id defines the unique id of the proposal. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_group_info**
> InlineResponse20054 cosmos_group_v1_group_info(group_id)

GroupInfo queries group info based on group id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
group_id = 'group_id_example' # str | group_id is the unique ID of the group.

try:
    # GroupInfo queries group info based on group id.
    api_response = api_instance.cosmos_group_v1_group_info(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_group_v1_group_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| group_id is the unique ID of the group. | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_group_members**
> InlineResponse20055 cosmos_group_v1_group_members(group_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GroupMembers queries members of a group by group id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
group_id = 'group_id_example' # str | group_id is the unique ID of the group.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GroupMembers queries members of a group by group id.
    api_response = api_instance.cosmos_group_v1_group_members(group_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_group_v1_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| group_id is the unique ID of the group. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_groups**
> InlineResponse20056 cosmos_group_v1_groups(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Groups queries all groups in state.

Since: cosmos-sdk 0.47.1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Groups queries all groups in state.
    api_response = api_instance.cosmos_group_v1_groups(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_group_v1_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_groups_by_admin**
> InlineResponse20057 cosmos_group_v1_groups_by_admin(admin, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GroupsByAdmin queries groups by admin address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
admin = 'admin_example' # str | admin is the account address of a group's admin.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GroupsByAdmin queries groups by admin address.
    api_response = api_instance.cosmos_group_v1_groups_by_admin(admin, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_group_v1_groups_by_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin** | **str**| admin is the account address of a group&#x27;s admin. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_groups_by_member**
> InlineResponse20058 cosmos_group_v1_groups_by_member(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GroupsByMember queries groups by member address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the group member address.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GroupsByMember queries groups by member address.
    api_response = api_instance.cosmos_group_v1_groups_by_member(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_group_v1_groups_by_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the group member address. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_mint_v1_beta1_annual_provisions**
> InlineResponse20059 cosmos_mint_v1_beta1_annual_provisions()

AnnualProvisions current minting annual provisions value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # AnnualProvisions current minting annual provisions value.
    api_response = api_instance.cosmos_mint_v1_beta1_annual_provisions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_mint_v1_beta1_annual_provisions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_mint_v1_beta1_inflation**
> InlineResponse20060 cosmos_mint_v1_beta1_inflation()

Inflation returns the current minting inflation value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Inflation returns the current minting inflation value.
    api_response = api_instance.cosmos_mint_v1_beta1_inflation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_mint_v1_beta1_inflation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_mint_v1_beta1_params**
> InlineResponse20061 cosmos_mint_v1_beta1_params()

Params returns the total set of minting parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params returns the total set of minting parameters.
    api_response = api_instance.cosmos_mint_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_mint_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_balance**
> QueryBalanceResponseIsTheResponseTypeForTheQueryBalanceRPCMethod cosmos_nft_v1_beta1_balance(owner, class_id)

Balance queries the number of NFTs of a given class owned by the owner, same as balanceOf in ERC721

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
owner = 'owner_example' # str | owner is the owner address of the nft
class_id = 'class_id_example' # str | class_id associated with the nft

try:
    # Balance queries the number of NFTs of a given class owned by the owner, same as balanceOf in ERC721
    api_response = api_instance.cosmos_nft_v1_beta1_balance(owner, class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner is the owner address of the nft | 
 **class_id** | **str**| class_id associated with the nft | 

### Return type

[**QueryBalanceResponseIsTheResponseTypeForTheQueryBalanceRPCMethod**](QueryBalanceResponseIsTheResponseTypeForTheQueryBalanceRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_class**
> QueryClassResponseIsTheResponseTypeForTheQueryClassRPCMethod cosmos_nft_v1_beta1_class(class_id)

Class queries an NFT class based on its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
class_id = 'class_id_example' # str | class_id associated with the nft

try:
    # Class queries an NFT class based on its id
    api_response = api_instance.cosmos_nft_v1_beta1_class(class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id associated with the nft | 

### Return type

[**QueryClassResponseIsTheResponseTypeForTheQueryClassRPCMethod**](QueryClassResponseIsTheResponseTypeForTheQueryClassRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_classes**
> QueryClassesResponseIsTheResponseTypeForTheQueryClassesRPCMethod cosmos_nft_v1_beta1_classes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Classes queries all NFT classes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Classes queries all NFT classes
    api_response = api_instance.cosmos_nft_v1_beta1_classes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryClassesResponseIsTheResponseTypeForTheQueryClassesRPCMethod**](QueryClassesResponseIsTheResponseTypeForTheQueryClassesRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_nft**
> QueryNFTResponseIsTheResponseTypeForTheQueryNFTRPCMethod cosmos_nft_v1_beta1_nft(class_id, id)

NFT queries an NFT based on its class and id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
class_id = 'class_id_example' # str | class_id associated with the nft
id = 'id_example' # str | id is a unique identifier of the NFT

try:
    # NFT queries an NFT based on its class and id.
    api_response = api_instance.cosmos_nft_v1_beta1_nft(class_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_nft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id associated with the nft | 
 **id** | **str**| id is a unique identifier of the NFT | 

### Return type

[**QueryNFTResponseIsTheResponseTypeForTheQueryNFTRPCMethod**](QueryNFTResponseIsTheResponseTypeForTheQueryNFTRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_nfts**
> QueryNFTsResponseIsTheResponseTypeForTheQueryNFTsRPCMethods cosmos_nft_v1_beta1_nfts(class_id=class_id, owner=owner, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

NFTs queries all NFTs of a given class or owner,choose at least one of the two, similar to tokenByIndex in ERC721Enumerable

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
class_id = 'class_id_example' # str | class_id associated with the nft (optional)
owner = 'owner_example' # str | owner is the owner address of the nft (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # NFTs queries all NFTs of a given class or owner,choose at least one of the two, similar to tokenByIndex in ERC721Enumerable
    api_response = api_instance.cosmos_nft_v1_beta1_nfts(class_id=class_id, owner=owner, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_nfts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id associated with the nft | [optional] 
 **owner** | **str**| owner is the owner address of the nft | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryNFTsResponseIsTheResponseTypeForTheQueryNFTsRPCMethods**](QueryNFTsResponseIsTheResponseTypeForTheQueryNFTsRPCMethods.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_owner**
> QueryOwnerResponseIsTheResponseTypeForTheQueryOwnerRPCMethod cosmos_nft_v1_beta1_owner(class_id, id)

Owner queries the owner of the NFT based on its class and id, same as ownerOf in ERC721

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
class_id = 'class_id_example' # str | class_id associated with the nft
id = 'id_example' # str | id is a unique identifier of the NFT

try:
    # Owner queries the owner of the NFT based on its class and id, same as ownerOf in ERC721
    api_response = api_instance.cosmos_nft_v1_beta1_owner(class_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id associated with the nft | 
 **id** | **str**| id is a unique identifier of the NFT | 

### Return type

[**QueryOwnerResponseIsTheResponseTypeForTheQueryOwnerRPCMethod**](QueryOwnerResponseIsTheResponseTypeForTheQueryOwnerRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_nft_v1_beta1_supply**
> QuerySupplyResponseIsTheResponseTypeForTheQuerySupplyRPCMethod cosmos_nft_v1_beta1_supply(class_id)

Supply queries the number of NFTs from the given class, same as totalSupply of ERC721.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
class_id = 'class_id_example' # str | class_id associated with the nft

try:
    # Supply queries the number of NFTs from the given class, same as totalSupply of ERC721.
    api_response = api_instance.cosmos_nft_v1_beta1_supply(class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_nft_v1_beta1_supply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id associated with the nft | 

### Return type

[**QuerySupplyResponseIsTheResponseTypeForTheQuerySupplyRPCMethod**](QuerySupplyResponseIsTheResponseTypeForTheQuerySupplyRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_params_v1_beta1_params**
> InlineResponse20062 cosmos_params_v1_beta1_params(subspace=subspace, key=key)

Params queries a specific parameter of a module, given its subspace and key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
subspace = 'subspace_example' # str | subspace defines the module to query the parameter for. (optional)
key = 'key_example' # str | key defines the key of the parameter in the subspace. (optional)

try:
    # Params queries a specific parameter of a module, given its subspace and key.
    api_response = api_instance.cosmos_params_v1_beta1_params(subspace=subspace, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_params_v1_beta1_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subspace** | **str**| subspace defines the module to query the parameter for. | [optional] 
 **key** | **str**| key defines the key of the parameter in the subspace. | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_params_v1_beta1_subspaces**
> InlineResponse20063 cosmos_params_v1_beta1_subspaces()

Subspaces queries for all registered subspaces and all keys for a subspace.

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Subspaces queries for all registered subspaces and all keys for a subspace.
    api_response = api_instance.cosmos_params_v1_beta1_subspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_params_v1_beta1_subspaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_slashing_v1_beta1_params**
> QueryParamsResponseIsTheResponseTypeForTheQueryParamsRPCMethod cosmos_slashing_v1_beta1_params()

Params queries the parameters of slashing module

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries the parameters of slashing module
    api_response = api_instance.cosmos_slashing_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_slashing_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryParamsResponseIsTheResponseTypeForTheQueryParamsRPCMethod**](QueryParamsResponseIsTheResponseTypeForTheQueryParamsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_slashing_v1_beta1_signing_info**
> QuerySigningInfoResponseIsTheResponseTypeForTheQuerySigningInfoRPCmethod cosmos_slashing_v1_beta1_signing_info(cons_address)

SigningInfo queries the signing info of given cons address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
cons_address = 'cons_address_example' # str | cons_address is the address to query signing info of

try:
    # SigningInfo queries the signing info of given cons address
    api_response = api_instance.cosmos_slashing_v1_beta1_signing_info(cons_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_slashing_v1_beta1_signing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cons_address** | **str**| cons_address is the address to query signing info of | 

### Return type

[**QuerySigningInfoResponseIsTheResponseTypeForTheQuerySigningInfoRPCmethod**](QuerySigningInfoResponseIsTheResponseTypeForTheQuerySigningInfoRPCmethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_slashing_v1_beta1_signing_infos**
> QuerySigningInfosResponseIsTheResponseTypeForTheQuerySigningInfosRPCmethod cosmos_slashing_v1_beta1_signing_infos(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

SigningInfos queries signing info of all validators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # SigningInfos queries signing info of all validators
    api_response = api_instance.cosmos_slashing_v1_beta1_signing_infos(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_slashing_v1_beta1_signing_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QuerySigningInfosResponseIsTheResponseTypeForTheQuerySigningInfosRPCmethod**](QuerySigningInfosResponseIsTheResponseTypeForTheQuerySigningInfosRPCmethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_delegation**
> InlineResponse20064 cosmos_staking_v1_beta1_delegation(delegator_addr)

Delegation queries delegate info for given validator delegator pair.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
delegator_addr = 'delegator_addr_example' # str | delegator_addr defines the delegator address to query for.

try:
    # Delegation queries delegate info for given validator delegator pair.
    api_response = api_instance.cosmos_staking_v1_beta1_delegation(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_delegation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| delegator_addr defines the delegator address to query for. | 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_fixed_deposit**
> InlineResponse20066 cosmos_staking_v1_beta1_fixed_deposit(id, address=address)

Queries a list of FixedDeposit items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
id = 'id_example' # str | 
address = 'address_example' # str |  (optional)

try:
    # Queries a list of FixedDeposit items.
    api_response = api_instance.cosmos_staking_v1_beta1_fixed_deposit(id, address=address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_fixed_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **address** | **str**|  | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_fixed_deposit_all**
> InlineResponse20065 cosmos_staking_v1_beta1_fixed_deposit_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    api_response = api_instance.cosmos_staking_v1_beta1_fixed_deposit_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_fixed_deposit_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_fixed_deposit_by_acct**
> InlineResponse20067 cosmos_staking_v1_beta1_fixed_deposit_by_acct(account, query_type)

Queries a list of FixedDepositByAcct items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
account = 'account_example' # str | cosmos.base.query.v1beta1.PageRequest pagination = 1;
query_type = 'query_type_example' # str | 

try:
    # Queries a list of FixedDepositByAcct items.
    api_response = api_instance.cosmos_staking_v1_beta1_fixed_deposit_by_acct(account, query_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_fixed_deposit_by_acct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| cosmos.base.query.v1beta1.PageRequest pagination &#x3D; 1; | 
 **query_type** | **str**|  | 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_fixed_deposit_by_region**
> InlineResponse20067 cosmos_staking_v1_beta1_fixed_deposit_by_region(regionid, query_type=query_type)

Queries a list of FixedDepositByRegion items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
regionid = 'regionid_example' # str | 
query_type = 'ALL_STATE' # str | cosmos.base.query.v1beta1.PageRequest pagination = 2; (optional) (default to ALL_STATE)

try:
    # Queries a list of FixedDepositByRegion items.
    api_response = api_instance.cosmos_staking_v1_beta1_fixed_deposit_by_region(regionid, query_type=query_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_fixed_deposit_by_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionid** | **str**|  | 
 **query_type** | **str**| cosmos.base.query.v1beta1.PageRequest pagination &#x3D; 2; | [optional] [default to ALL_STATE]

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_fixed_deposit_interest_rate**
> InlineResponse20068 cosmos_staking_v1_beta1_fixed_deposit_interest_rate(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Queries FixedDepositInterest Item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Queries FixedDepositInterest Item.
    api_response = api_instance.cosmos_staking_v1_beta1_fixed_deposit_interest_rate(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_fixed_deposit_interest_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_historical_info**
> InlineResponse20069 cosmos_staking_v1_beta1_historical_info(height)

HistoricalInfo queries the historical info for given height.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
height = 'height_example' # str | height defines at which height to query the historical info.

try:
    # HistoricalInfo queries the historical info for given height.
    api_response = api_instance.cosmos_staking_v1_beta1_historical_info(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_historical_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **str**| height defines at which height to query the historical info. | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_kyc**
> InlineResponse20071 cosmos_staking_v1_beta1_kyc(account)

Queries a list of Kyc items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
account = 'account_example' # str | 

try:
    # Queries a list of Kyc items.
    api_response = api_instance.cosmos_staking_v1_beta1_kyc(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_kyc_all**
> InlineResponse20070 cosmos_staking_v1_beta1_kyc_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    api_response = api_instance.cosmos_staking_v1_beta1_kyc_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_kyc_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_kyc_by_region**
> InlineResponse20070 cosmos_staking_v1_beta1_kyc_by_region(region_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Queries a list of KycByRegion items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
region_id = 'region_id_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Queries a list of KycByRegion items.
    api_response = api_instance.cosmos_staking_v1_beta1_kyc_by_region(region_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_kyc_by_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_params**
> InlineResponse20072 cosmos_staking_v1_beta1_params()

Parameters queries the staking parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Parameters queries the staking parameters.
    api_response = api_instance.cosmos_staking_v1_beta1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_pool**
> InlineResponse20073 cosmos_staking_v1_beta1_pool()

Pool queries the pool info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Pool queries the pool info.
    api_response = api_instance.cosmos_staking_v1_beta1_pool()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_pool: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_region**
> InlineResponse20075 cosmos_staking_v1_beta1_region(region_id)

Queries a list of Region items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
region_id = 'region_id_example' # str | 

try:
    # Queries a list of Region items.
    api_response = api_instance.cosmos_staking_v1_beta1_region(region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**|  | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_region_all**
> InlineResponse20074 cosmos_staking_v1_beta1_region_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    api_response = api_instance.cosmos_staking_v1_beta1_region_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_region_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_siid**
> InlineResponse20077 cosmos_staking_v1_beta1_siid(siid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
siid = 'siid_example' # str | 

try:
    api_response = api_instance.cosmos_staking_v1_beta1_siid(siid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_siid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siid** | **str**|  | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_siid_all**
> InlineResponse20076 cosmos_staking_v1_beta1_siid_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    api_response = api_instance.cosmos_staking_v1_beta1_siid_all(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_siid_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_siid_by_account**
> InlineResponse20077 cosmos_staking_v1_beta1_siid_by_account(account)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
account = 'account_example' # str | 

try:
    api_response = api_instance.cosmos_staking_v1_beta1_siid_by_account(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_siid_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_unbonding_delegation**
> InlineResponse20078 cosmos_staking_v1_beta1_unbonding_delegation(delegator_addr)

UnbondingDelegation queries unbonding info for given validator delegator pair.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
delegator_addr = 'delegator_addr_example' # str | delegator_addr defines the delegator address to query for.

try:
    # UnbondingDelegation queries unbonding info for given validator delegator pair.
    api_response = api_instance.cosmos_staking_v1_beta1_unbonding_delegation(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_unbonding_delegation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| delegator_addr defines the delegator address to query for. | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_validator**
> QueryValidatorResponseIsResponseTypeForTheQueryValidatorRPCMethod cosmos_staking_v1_beta1_validator(validator_addr)

Validator queries validator info for given validator address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
validator_addr = 'validator_addr_example' # str | validator_addr defines the validator address to query for.

try:
    # Validator queries validator info for given validator address.
    api_response = api_instance.cosmos_staking_v1_beta1_validator(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| validator_addr defines the validator address to query for. | 

### Return type

[**QueryValidatorResponseIsResponseTypeForTheQueryValidatorRPCMethod**](QueryValidatorResponseIsResponseTypeForTheQueryValidatorRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_validator_delegations**
> QueryValidatorDelegationsResponseIsResponseTypeForTheQueryValidatorDelegationsRPCMethod cosmos_staking_v1_beta1_validator_delegations(validator_addr, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ValidatorDelegations queries delegate info for given validator.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
validator_addr = 'validator_addr_example' # str | validator_addr defines the validator address to query for.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ValidatorDelegations queries delegate info for given validator.
    api_response = api_instance.cosmos_staking_v1_beta1_validator_delegations(validator_addr, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_validator_delegations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| validator_addr defines the validator address to query for. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryValidatorDelegationsResponseIsResponseTypeForTheQueryValidatorDelegationsRPCMethod**](QueryValidatorDelegationsResponseIsResponseTypeForTheQueryValidatorDelegationsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_staking_v1_beta1_validators**
> QueryValidatorsResponseIsResponseTypeForTheQueryValidatorsRPCMethod cosmos_staking_v1_beta1_validators(status=status, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Validators queries all validators that match the given status.

When called from another module, this query might consume a high amount of gas if the pagination field is incorrectly set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
status = 'status_example' # str | status enables to query for validators matching a given status. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Validators queries all validators that match the given status.
    api_response = api_instance.cosmos_staking_v1_beta1_validators(status=status, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_staking_v1_beta1_validators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| status enables to query for validators matching a given status. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryValidatorsResponseIsResponseTypeForTheQueryValidatorsRPCMethod**](QueryValidatorsResponseIsResponseTypeForTheQueryValidatorsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_upgrade_v1_beta1_applied_plan**
> InlineResponse20084 cosmos_upgrade_v1_beta1_applied_plan(name)

AppliedPlan queries a previously applied upgrade plan by its name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
name = 'name_example' # str | name is the name of the applied plan to query for.

try:
    # AppliedPlan queries a previously applied upgrade plan by its name.
    api_response = api_instance.cosmos_upgrade_v1_beta1_applied_plan(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_upgrade_v1_beta1_applied_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name is the name of the applied plan to query for. | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_upgrade_v1_beta1_authority**
> QueryAuthorityResponseIsTheResponseTypeForQueryAuthority cosmos_upgrade_v1_beta1_authority()

Returns the account with authority to conduct upgrades

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Returns the account with authority to conduct upgrades
    api_response = api_instance.cosmos_upgrade_v1_beta1_authority()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_upgrade_v1_beta1_authority: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryAuthorityResponseIsTheResponseTypeForQueryAuthority**](QueryAuthorityResponseIsTheResponseTypeForQueryAuthority.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_upgrade_v1_beta1_current_plan**
> InlineResponse20085 cosmos_upgrade_v1_beta1_current_plan()

CurrentPlan queries the current upgrade plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # CurrentPlan queries the current upgrade plan.
    api_response = api_instance.cosmos_upgrade_v1_beta1_current_plan()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_upgrade_v1_beta1_current_plan: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_upgrade_v1_beta1_module_versions**
> InlineResponse20086 cosmos_upgrade_v1_beta1_module_versions(module_name=module_name)

ModuleVersions queries the list of module versions from state.

Since: cosmos-sdk 0.43

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
module_name = 'module_name_example' # str | module_name is a field to query a specific module consensus version from state. Leaving this empty will fetch the full list of module versions from state (optional)

try:
    # ModuleVersions queries the list of module versions from state.
    api_response = api_instance.cosmos_upgrade_v1_beta1_module_versions(module_name=module_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_upgrade_v1_beta1_module_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| module_name is a field to query a specific module consensus version from state. Leaving this empty will fetch the full list of module versions from state | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_upgrade_v1_beta1_upgraded_consensus_state**
> InlineResponse20087 cosmos_upgrade_v1_beta1_upgraded_consensus_state(last_height)

UpgradedConsensusState queries the consensus state that will serve as a trusted kernel for the next version of this chain. It will only be stored at the last height of this chain. UpgradedConsensusState RPC not supported with legacy querier This rpc is deprecated now that IBC has its own replacement (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
last_height = 'last_height_example' # str | last height of the current chain must be sent in request as this is the height under which next consensus state is stored

try:
    # UpgradedConsensusState queries the consensus state that will serve as a trusted kernel for the next version of this chain. It will only be stored at the last height of this chain. UpgradedConsensusState RPC not supported with legacy querier This rpc is deprecated now that IBC has its own replacement (https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)
    api_response = api_instance.cosmos_upgrade_v1_beta1_upgraded_consensus_state(last_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmos_upgrade_v1_beta1_upgraded_consensus_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_height** | **str**| last height of the current chain must be sent in request as this is the height under which next consensus state is stored | 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_all_contract_state**
> QueryAllContractStateResponseIsTheResponseTypeForTheQueryAllContractStateRPCMethod cosmwasm_wasm_v1_all_contract_state(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

AllContractState gets all raw store data for a single contract

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address of the contract
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # AllContractState gets all raw store data for a single contract
    api_response = api_instance.cosmwasm_wasm_v1_all_contract_state(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_all_contract_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address of the contract | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryAllContractStateResponseIsTheResponseTypeForTheQueryAllContractStateRPCMethod**](QueryAllContractStateResponseIsTheResponseTypeForTheQueryAllContractStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_code**
> QueryCodeResponseIsTheResponseTypeForTheQueryCodeRPCMethod cosmwasm_wasm_v1_code(code_id)

Code gets the binary code and metadata for a singe wasm code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
code_id = 'code_id_example' # str | grpc-gateway_out does not support Go style CodID

try:
    # Code gets the binary code and metadata for a singe wasm code
    api_response = api_instance.cosmwasm_wasm_v1_code(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **str**| grpc-gateway_out does not support Go style CodID | 

### Return type

[**QueryCodeResponseIsTheResponseTypeForTheQueryCodeRPCMethod**](QueryCodeResponseIsTheResponseTypeForTheQueryCodeRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_codes**
> QueryCodesResponseIsTheResponseTypeForTheQueryCodesRPCMethod cosmwasm_wasm_v1_codes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Codes gets the metadata for all stored wasm codes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Codes gets the metadata for all stored wasm codes
    api_response = api_instance.cosmwasm_wasm_v1_codes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryCodesResponseIsTheResponseTypeForTheQueryCodesRPCMethod**](QueryCodesResponseIsTheResponseTypeForTheQueryCodesRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_contract_history**
> QueryContractHistoryResponseIsTheResponseTypeForTheQueryContractHistoryRPCMethod cosmwasm_wasm_v1_contract_history(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ContractHistory gets the contract code history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address of the contract to query
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ContractHistory gets the contract code history
    api_response = api_instance.cosmwasm_wasm_v1_contract_history(address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_contract_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address of the contract to query | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryContractHistoryResponseIsTheResponseTypeForTheQueryContractHistoryRPCMethod**](QueryContractHistoryResponseIsTheResponseTypeForTheQueryContractHistoryRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_contract_info**
> QueryContractInfoResponseIsTheResponseTypeForTheQueryContractInfoRPCmethod cosmwasm_wasm_v1_contract_info(address)

ContractInfo gets the contract meta data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address of the contract to query

try:
    # ContractInfo gets the contract meta data
    api_response = api_instance.cosmwasm_wasm_v1_contract_info(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_contract_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address of the contract to query | 

### Return type

[**QueryContractInfoResponseIsTheResponseTypeForTheQueryContractInfoRPCmethod**](QueryContractInfoResponseIsTheResponseTypeForTheQueryContractInfoRPCmethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_contracts_by_code**
> QueryContractsByCodeResponseIsTheResponseTypeForTheQueryContractsByCodeRPCMethod cosmwasm_wasm_v1_contracts_by_code(code_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ContractsByCode lists all smart contracts for a code id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
code_id = 'code_id_example' # str | grpc-gateway_out does not support Go style CodID
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ContractsByCode lists all smart contracts for a code id
    api_response = api_instance.cosmwasm_wasm_v1_contracts_by_code(code_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_contracts_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **str**| grpc-gateway_out does not support Go style CodID | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryContractsByCodeResponseIsTheResponseTypeForTheQueryContractsByCodeRPCMethod**](QueryContractsByCodeResponseIsTheResponseTypeForTheQueryContractsByCodeRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_contracts_by_creator**
> InlineResponse20089 cosmwasm_wasm_v1_contracts_by_creator(creator_address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ContractsByCreator gets the contracts by creator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
creator_address = 'creator_address_example' # str | CreatorAddress is the address of contract creator
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ContractsByCreator gets the contracts by creator
    api_response = api_instance.cosmwasm_wasm_v1_contracts_by_creator(creator_address, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_contracts_by_creator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creator_address** | **str**| CreatorAddress is the address of contract creator | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_params**
> InlineResponse20088 cosmwasm_wasm_v1_params()

Params gets the module params

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params gets the module params
    api_response = api_instance.cosmwasm_wasm_v1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_pinned_codes**
> QueryPinnedCodesResponseIsTheResponseTypeForTheQueryPinnedCodesRPCMethod cosmwasm_wasm_v1_pinned_codes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

PinnedCodes gets the pinned code ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # PinnedCodes gets the pinned code ids
    api_response = api_instance.cosmwasm_wasm_v1_pinned_codes(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_pinned_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryPinnedCodesResponseIsTheResponseTypeForTheQueryPinnedCodesRPCMethod**](QueryPinnedCodesResponseIsTheResponseTypeForTheQueryPinnedCodesRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_raw_contract_state**
> QueryRawContractStateResponseIsTheResponseTypeForTheQueryRawContractStateRPCMethod cosmwasm_wasm_v1_raw_contract_state(address, query_data)

RawContractState gets single key from the raw store data of a contract

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address of the contract
query_data = 'B' # str | 

try:
    # RawContractState gets single key from the raw store data of a contract
    api_response = api_instance.cosmwasm_wasm_v1_raw_contract_state(address, query_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_raw_contract_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address of the contract | 
 **query_data** | **str**|  | 

### Return type

[**QueryRawContractStateResponseIsTheResponseTypeForTheQueryRawContractStateRPCMethod**](QueryRawContractStateResponseIsTheResponseTypeForTheQueryRawContractStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmwasm_wasm_v1_smart_contract_state**
> QuerySmartContractStateResponseIsTheResponseTypeForTheQuerySmartContractStateRPCMethod cosmwasm_wasm_v1_smart_contract_state(address, query_data)

SmartContractState get smart query result from the contract

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
address = 'address_example' # str | address is the address of the contract
query_data = 'B' # str | QueryData contains the query data passed to the contract

try:
    # SmartContractState get smart query result from the contract
    api_response = api_instance.cosmwasm_wasm_v1_smart_contract_state(address, query_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->cosmwasm_wasm_v1_smart_contract_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address is the address of the contract | 
 **query_data** | **str**| QueryData contains the query data passed to the contract | 

### Return type

[**QuerySmartContractStateResponseIsTheResponseTypeForTheQuerySmartContractStateRPCMethod**](QuerySmartContractStateResponseIsTheResponseTypeForTheQuerySmartContractStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_counterparty_payee**
> QueryCounterpartyPayeeResponseDefinesTheResponseTypeForTheCounterpartyPayeeRpc ibc_applications_fee_v1_counterparty_payee(channel_id, relayer)

CounterpartyPayee returns the registered counterparty payee for forward relaying

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | unique channel identifier
relayer = 'relayer_example' # str | the relayer address to which the counterparty is registered

try:
    # CounterpartyPayee returns the registered counterparty payee for forward relaying
    api_response = api_instance.ibc_applications_fee_v1_counterparty_payee(channel_id, relayer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_counterparty_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| unique channel identifier | 
 **relayer** | **str**| the relayer address to which the counterparty is registered | 

### Return type

[**QueryCounterpartyPayeeResponseDefinesTheResponseTypeForTheCounterpartyPayeeRpc**](QueryCounterpartyPayeeResponseDefinesTheResponseTypeForTheCounterpartyPayeeRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_fee_enabled_channel**
> QueryFeeEnabledChannelResponseDefinesTheResponseTypeForTheFeeEnabledChannelRpc ibc_applications_fee_v1_fee_enabled_channel(channel_id, port_id)

FeeEnabledChannel returns true if the provided port and channel identifiers belong to a fee enabled channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | unique channel identifier
port_id = 'port_id_example' # str | unique port identifier

try:
    # FeeEnabledChannel returns true if the provided port and channel identifiers belong to a fee enabled channel
    api_response = api_instance.ibc_applications_fee_v1_fee_enabled_channel(channel_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_fee_enabled_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| unique channel identifier | 
 **port_id** | **str**| unique port identifier | 

### Return type

[**QueryFeeEnabledChannelResponseDefinesTheResponseTypeForTheFeeEnabledChannelRpc**](QueryFeeEnabledChannelResponseDefinesTheResponseTypeForTheFeeEnabledChannelRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_fee_enabled_channels**
> QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc ibc_applications_fee_v1_fee_enabled_channels(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)

FeeEnabledChannels returns a list of all fee enabled channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)
query_height = 'query_height_example' # str | block height at which to query (optional)

try:
    # FeeEnabledChannels returns a list of all fee enabled channels
    api_response = api_instance.ibc_applications_fee_v1_fee_enabled_channels(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_fee_enabled_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 
 **query_height** | **str**| block height at which to query | [optional] 

### Return type

[**QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc**](QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_incentivized_packet**
> QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketRpc ibc_applications_fee_v1_incentivized_packet(packet_id_channel_id, packet_id_port_id, packet_id_sequence, query_height=query_height)

IncentivizedPacket returns all packet fees for a packet given its identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
packet_id_channel_id = 'packet_id_channel_id_example' # str | channel unique identifier
packet_id_port_id = 'packet_id_port_id_example' # str | channel port identifier
packet_id_sequence = 'packet_id_sequence_example' # str | packet sequence
query_height = 'query_height_example' # str | block height at which to query (optional)

try:
    # IncentivizedPacket returns all packet fees for a packet given its identifier
    api_response = api_instance.ibc_applications_fee_v1_incentivized_packet(packet_id_channel_id, packet_id_port_id, packet_id_sequence, query_height=query_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_incentivized_packet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packet_id_channel_id** | **str**| channel unique identifier | 
 **packet_id_port_id** | **str**| channel port identifier | 
 **packet_id_sequence** | **str**| packet sequence | 
 **query_height** | **str**| block height at which to query | [optional] 

### Return type

[**QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketRpc**](QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_incentivized_packets**
> QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRpc ibc_applications_fee_v1_incentivized_packets(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)

IncentivizedPackets returns all incentivized packets and their associated fees

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)
query_height = 'query_height_example' # str | block height at which to query (optional)

try:
    # IncentivizedPackets returns all incentivized packets and their associated fees
    api_response = api_instance.ibc_applications_fee_v1_incentivized_packets(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_incentivized_packets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 
 **query_height** | **str**| block height at which to query | [optional] 

### Return type

[**QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRpc**](QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_incentivized_packets_for_channel**
> QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRPC ibc_applications_fee_v1_incentivized_packets_for_channel(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)

Gets all incentivized packets for a specific channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | 
port_id = 'port_id_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)
query_height = 'query_height_example' # str | Height to query at (optional)

try:
    # Gets all incentivized packets for a specific channel
    api_response = api_instance.ibc_applications_fee_v1_incentivized_packets_for_channel(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, query_height=query_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_incentivized_packets_for_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **port_id** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 
 **query_height** | **str**| Height to query at | [optional] 

### Return type

[**QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRPC**](QueryIncentivizedPacketsResponseDefinesTheResponseTypeForTheIncentivizedPacketsRPC.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_payee**
> QueryPayeeResponseDefinesTheResponseTypeForThePayeeRpc ibc_applications_fee_v1_payee(channel_id, relayer)

Payee returns the registered payee address for a specific channel given the relayer address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | unique channel identifier
relayer = 'relayer_example' # str | the relayer address to which the distribution address is registered

try:
    # Payee returns the registered payee address for a specific channel given the relayer address
    api_response = api_instance.ibc_applications_fee_v1_payee(channel_id, relayer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| unique channel identifier | 
 **relayer** | **str**| the relayer address to which the distribution address is registered | 

### Return type

[**QueryPayeeResponseDefinesTheResponseTypeForThePayeeRpc**](QueryPayeeResponseDefinesTheResponseTypeForThePayeeRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_total_ack_fees**
> QueryTotalAckFeesResponseDefinesTheResponseTypeForTheTotalAckFeesRpc ibc_applications_fee_v1_total_ack_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)

TotalAckFees returns the total acknowledgement fees for a packet given its identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
packet_id_channel_id = 'packet_id_channel_id_example' # str | channel unique identifier
packet_id_port_id = 'packet_id_port_id_example' # str | channel port identifier
packet_id_sequence = 'packet_id_sequence_example' # str | packet sequence

try:
    # TotalAckFees returns the total acknowledgement fees for a packet given its identifier
    api_response = api_instance.ibc_applications_fee_v1_total_ack_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_total_ack_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packet_id_channel_id** | **str**| channel unique identifier | 
 **packet_id_port_id** | **str**| channel port identifier | 
 **packet_id_sequence** | **str**| packet sequence | 

### Return type

[**QueryTotalAckFeesResponseDefinesTheResponseTypeForTheTotalAckFeesRpc**](QueryTotalAckFeesResponseDefinesTheResponseTypeForTheTotalAckFeesRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_total_recv_fees**
> QueryTotalRecvFeesResponseDefinesTheResponseTypeForTheTotalRecvFeesRpc ibc_applications_fee_v1_total_recv_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)

TotalRecvFees returns the total receive fees for a packet given its identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
packet_id_channel_id = 'packet_id_channel_id_example' # str | channel unique identifier
packet_id_port_id = 'packet_id_port_id_example' # str | channel port identifier
packet_id_sequence = 'packet_id_sequence_example' # str | packet sequence

try:
    # TotalRecvFees returns the total receive fees for a packet given its identifier
    api_response = api_instance.ibc_applications_fee_v1_total_recv_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_total_recv_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packet_id_channel_id** | **str**| channel unique identifier | 
 **packet_id_port_id** | **str**| channel port identifier | 
 **packet_id_sequence** | **str**| packet sequence | 

### Return type

[**QueryTotalRecvFeesResponseDefinesTheResponseTypeForTheTotalRecvFeesRpc**](QueryTotalRecvFeesResponseDefinesTheResponseTypeForTheTotalRecvFeesRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_fee_v1_total_timeout_fees**
> QueryTotalTimeoutFeesResponseDefinesTheResponseTypeForTheTotalTimeoutFeesRpc ibc_applications_fee_v1_total_timeout_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)

TotalTimeoutFees returns the total timeout fees for a packet given its identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
packet_id_channel_id = 'packet_id_channel_id_example' # str | channel unique identifier
packet_id_port_id = 'packet_id_port_id_example' # str | channel port identifier
packet_id_sequence = 'packet_id_sequence_example' # str | packet sequence

try:
    # TotalTimeoutFees returns the total timeout fees for a packet given its identifier
    api_response = api_instance.ibc_applications_fee_v1_total_timeout_fees(packet_id_channel_id, packet_id_port_id, packet_id_sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_fee_v1_total_timeout_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packet_id_channel_id** | **str**| channel unique identifier | 
 **packet_id_port_id** | **str**| channel port identifier | 
 **packet_id_sequence** | **str**| packet sequence | 

### Return type

[**QueryTotalTimeoutFeesResponseDefinesTheResponseTypeForTheTotalTimeoutFeesRpc**](QueryTotalTimeoutFeesResponseDefinesTheResponseTypeForTheTotalTimeoutFeesRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_interchain_accounts_controller_v1_interchain_account**
> InlineResponse20090 ibc_applications_interchain_accounts_controller_v1_interchain_account(owner, connection_id)

InterchainAccount returns the interchain account address for a given owner address on a given connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
owner = 'owner_example' # str | 
connection_id = 'connection_id_example' # str | 

try:
    # InterchainAccount returns the interchain account address for a given owner address on a given connection
    api_response = api_instance.ibc_applications_interchain_accounts_controller_v1_interchain_account(owner, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_interchain_accounts_controller_v1_interchain_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **connection_id** | **str**|  | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_interchain_accounts_controller_v1_params**
> InlineResponse20091 ibc_applications_interchain_accounts_controller_v1_params()

Params queries all parameters of the ICA controller submodule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries all parameters of the ICA controller submodule.
    api_response = api_instance.ibc_applications_interchain_accounts_controller_v1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_interchain_accounts_controller_v1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_interchain_accounts_host_v1_params**
> InlineResponse20092 ibc_applications_interchain_accounts_host_v1_params()

Params queries all parameters of the ICA host submodule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries all parameters of the ICA host submodule.
    api_response = api_instance.ibc_applications_interchain_accounts_host_v1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_interchain_accounts_host_v1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_denom_hash**
> InlineResponse20094 ibc_applications_transfer_v1_denom_hash(trace)

DenomHash queries a denomination hash information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
trace = 'trace_example' # str | The denomination trace ([port_id]/[channel_id])+/[denom]

try:
    # DenomHash queries a denomination hash information.
    api_response = api_instance.ibc_applications_transfer_v1_denom_hash(trace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_denom_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace** | **str**| The denomination trace ([port_id]/[channel_id])+/[denom] | 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_denom_trace**
> InlineResponse20096 ibc_applications_transfer_v1_denom_trace(hash)

DenomTrace queries a denomination trace information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
hash = 'hash_example' # str | hash (in hex format) or denom (full denom with ibc prefix) of the denomination trace information.

try:
    # DenomTrace queries a denomination trace information.
    api_response = api_instance.ibc_applications_transfer_v1_denom_trace(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_denom_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| hash (in hex format) or denom (full denom with ibc prefix) of the denomination trace information. | 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_denom_traces**
> InlineResponse20095 ibc_applications_transfer_v1_denom_traces(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

DenomTraces queries all denomination traces.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # DenomTraces queries all denomination traces.
    api_response = api_instance.ibc_applications_transfer_v1_denom_traces(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_denom_traces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_escrow_address**
> InlineResponse20093 ibc_applications_transfer_v1_escrow_address(channel_id, port_id)

EscrowAddress returns the escrow address for a particular port and channel id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | unique channel identifier
port_id = 'port_id_example' # str | unique port identifier

try:
    # EscrowAddress returns the escrow address for a particular port and channel id.
    api_response = api_instance.ibc_applications_transfer_v1_escrow_address(channel_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_escrow_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| unique channel identifier | 
 **port_id** | **str**| unique port identifier | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_params**
> InlineResponse20098 ibc_applications_transfer_v1_params()

Params queries all parameters of the ibc-transfer module.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # Params queries all parameters of the ibc-transfer module.
    api_response = api_instance.ibc_applications_transfer_v1_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_applications_transfer_v1_total_escrow_for_denom**
> InlineResponse20097 ibc_applications_transfer_v1_total_escrow_for_denom(denom)

TotalEscrowForDenom returns the total amount of tokens in escrow based on the denom.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
denom = 'denom_example' # str | 

try:
    # TotalEscrowForDenom returns the total amount of tokens in escrow based on the denom.
    api_response = api_instance.ibc_applications_transfer_v1_total_escrow_for_denom(denom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_applications_transfer_v1_total_escrow_for_denom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denom** | **str**|  | 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_channel**
> InlineResponse200100 ibc_core_channel_v1_channel(channel_id, port_id)

Channel queries an IBC Channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier

try:
    # Channel queries an IBC Channel.
    api_response = api_instance.ibc_core_channel_v1_channel(channel_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_channel_client_state**
> QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod ibc_core_channel_v1_channel_client_state(channel_id, port_id)

ChannelClientState queries for the client state for the channel associated with the provided channel identifiers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier

try:
    # ChannelClientState queries for the client state for the channel associated with the provided channel identifiers.
    api_response = api_instance.ibc_core_channel_v1_channel_client_state(channel_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_channel_client_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 

### Return type

[**QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod**](QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_channel_consensus_state**
> QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod1 ibc_core_channel_v1_channel_consensus_state(channel_id, port_id, revision_number, revision_height)

ChannelConsensusState queries for the consensus state for the channel associated with the provided channel identifiers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
revision_number = 'revision_number_example' # str | revision number of the consensus state
revision_height = 'revision_height_example' # str | revision height of the consensus state

try:
    # ChannelConsensusState queries for the consensus state for the channel associated with the provided channel identifiers.
    api_response = api_instance.ibc_core_channel_v1_channel_consensus_state(channel_id, port_id, revision_number, revision_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_channel_consensus_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **revision_number** | **str**| revision number of the consensus state | 
 **revision_height** | **str**| revision height of the consensus state | 

### Return type

[**QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod1**](QueryChannelClientStateResponseIsTheResponseTypeForTheQueryQueryChannelClientStateRPCMethod1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_channels**
> InlineResponse20099 ibc_core_channel_v1_channels(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Channels queries all the IBC channels of a chain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Channels queries all the IBC channels of a chain.
    api_response = api_instance.ibc_core_channel_v1_channels(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_connection_channels**
> QueryConnectionChannelsResponseIsTheResponseTypeForTheQueryQueryConnectionChannelsRPCMethod ibc_core_channel_v1_connection_channels(connection, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ConnectionChannels queries all the channels associated with a connection end.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
connection = 'connection_example' # str | connection unique identifier
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ConnectionChannels queries all the channels associated with a connection end.
    api_response = api_instance.ibc_core_channel_v1_connection_channels(connection, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_connection_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**| connection unique identifier | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryConnectionChannelsResponseIsTheResponseTypeForTheQueryQueryConnectionChannelsRPCMethod**](QueryConnectionChannelsResponseIsTheResponseTypeForTheQueryQueryConnectionChannelsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_next_sequence_receive**
> QuerySequenceResponseIsTheRequestTypeForTheQueryQueryNextSequenceReceiveResponseRPCMethod ibc_core_channel_v1_next_sequence_receive(channel_id, port_id)

NextSequenceReceive returns the next receive sequence for a given channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier

try:
    # NextSequenceReceive returns the next receive sequence for a given channel.
    api_response = api_instance.ibc_core_channel_v1_next_sequence_receive(channel_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_next_sequence_receive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 

### Return type

[**QuerySequenceResponseIsTheRequestTypeForTheQueryQueryNextSequenceReceiveResponseRPCMethod**](QuerySequenceResponseIsTheRequestTypeForTheQueryQueryNextSequenceReceiveResponseRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_packet_acknowledgement**
> QueryPacketAcknowledgementResponseDefinesTheClientQueryResponseForApacketWhichAlsoIncludesAProofAndTheHeightFromWhichTheproofWasRetrieved ibc_core_channel_v1_packet_acknowledgement(channel_id, port_id, sequence)

PacketAcknowledgement queries a stored packet acknowledgement hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
sequence = 'sequence_example' # str | packet sequence

try:
    # PacketAcknowledgement queries a stored packet acknowledgement hash.
    api_response = api_instance.ibc_core_channel_v1_packet_acknowledgement(channel_id, port_id, sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_packet_acknowledgement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **sequence** | **str**| packet sequence | 

### Return type

[**QueryPacketAcknowledgementResponseDefinesTheClientQueryResponseForApacketWhichAlsoIncludesAProofAndTheHeightFromWhichTheproofWasRetrieved**](QueryPacketAcknowledgementResponseDefinesTheClientQueryResponseForApacketWhichAlsoIncludesAProofAndTheHeightFromWhichTheproofWasRetrieved.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_packet_acknowledgements**
> QueryPacketAcknowledgemetsResponseIsTheRequestTypeForTheQueryQueryPacketAcknowledgementsRPCMethod ibc_core_channel_v1_packet_acknowledgements(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, packet_commitment_sequences=packet_commitment_sequences)

PacketAcknowledgements returns all the packet acknowledgements associated with a channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)
packet_commitment_sequences = ['packet_commitment_sequences_example'] # list[str] | list of packet sequences (optional)

try:
    # PacketAcknowledgements returns all the packet acknowledgements associated with a channel.
    api_response = api_instance.ibc_core_channel_v1_packet_acknowledgements(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, packet_commitment_sequences=packet_commitment_sequences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_packet_acknowledgements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 
 **packet_commitment_sequences** | [**list[str]**](str.md)| list of packet sequences | [optional] 

### Return type

[**QueryPacketAcknowledgemetsResponseIsTheRequestTypeForTheQueryQueryPacketAcknowledgementsRPCMethod**](QueryPacketAcknowledgemetsResponseIsTheRequestTypeForTheQueryQueryPacketAcknowledgementsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_packet_commitment**
> QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved ibc_core_channel_v1_packet_commitment(channel_id, port_id, sequence)

PacketCommitment queries a stored packet commitment hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
sequence = 'sequence_example' # str | packet sequence

try:
    # PacketCommitment queries a stored packet commitment hash.
    api_response = api_instance.ibc_core_channel_v1_packet_commitment(channel_id, port_id, sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_packet_commitment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **sequence** | **str**| packet sequence | 

### Return type

[**QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved**](QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_packet_commitments**
> QueryPacketCommitmentsResponseIsTheRequestTypeForTheQueryQueryPacketCommitmentsRPCMethod ibc_core_channel_v1_packet_commitments(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

PacketCommitments returns all the packet commitments hashes associated with a channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # PacketCommitments returns all the packet commitments hashes associated with a channel.
    api_response = api_instance.ibc_core_channel_v1_packet_commitments(channel_id, port_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_packet_commitments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryPacketCommitmentsResponseIsTheRequestTypeForTheQueryQueryPacketCommitmentsRPCMethod**](QueryPacketCommitmentsResponseIsTheRequestTypeForTheQueryQueryPacketCommitmentsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_packet_receipt**
> QueryPacketReceiptResponseDefinesTheClientQueryResponseForAPacketreceiptWhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved ibc_core_channel_v1_packet_receipt(channel_id, port_id, sequence)

PacketReceipt queries if a given packet sequence has been received on the queried chain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
sequence = 'sequence_example' # str | packet sequence

try:
    # PacketReceipt queries if a given packet sequence has been received on the queried chain
    api_response = api_instance.ibc_core_channel_v1_packet_receipt(channel_id, port_id, sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_packet_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **sequence** | **str**| packet sequence | 

### Return type

[**QueryPacketReceiptResponseDefinesTheClientQueryResponseForAPacketreceiptWhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved**](QueryPacketReceiptResponseDefinesTheClientQueryResponseForAPacketreceiptWhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_unreceived_acks**
> QueryUnreceivedAcksResponseIsTheResponseTypeForTheQueryUnreceivedAcksRPCMethod ibc_core_channel_v1_unreceived_acks(channel_id, port_id, packet_ack_sequences)

UnreceivedAcks returns all the unreceived IBC acknowledgements associated with a channel and sequences.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
packet_ack_sequences = ['packet_ack_sequences_example'] # list[str] | list of acknowledgement sequences

try:
    # UnreceivedAcks returns all the unreceived IBC acknowledgements associated with a channel and sequences.
    api_response = api_instance.ibc_core_channel_v1_unreceived_acks(channel_id, port_id, packet_ack_sequences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_unreceived_acks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **packet_ack_sequences** | [**list[str]**](str.md)| list of acknowledgement sequences | 

### Return type

[**QueryUnreceivedAcksResponseIsTheResponseTypeForTheQueryUnreceivedAcksRPCMethod**](QueryUnreceivedAcksResponseIsTheResponseTypeForTheQueryUnreceivedAcksRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_channel_v1_unreceived_packets**
> QueryUnreceivedPacketsResponseIsTheResponseTypeForTheQueryUnreceivedPacketCommitmentsRPCMethod ibc_core_channel_v1_unreceived_packets(channel_id, port_id, packet_commitment_sequences)

UnreceivedPackets returns all the unreceived IBC packets associated with a channel and sequences.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
channel_id = 'channel_id_example' # str | channel unique identifier
port_id = 'port_id_example' # str | port unique identifier
packet_commitment_sequences = ['packet_commitment_sequences_example'] # list[str] | list of packet sequences

try:
    # UnreceivedPackets returns all the unreceived IBC packets associated with a channel and sequences.
    api_response = api_instance.ibc_core_channel_v1_unreceived_packets(channel_id, port_id, packet_commitment_sequences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_channel_v1_unreceived_packets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channel unique identifier | 
 **port_id** | **str**| port unique identifier | 
 **packet_commitment_sequences** | [**list[str]**](str.md)| list of packet sequences | 

### Return type

[**QueryUnreceivedPacketsResponseIsTheResponseTypeForTheQueryUnreceivedPacketCommitmentsRPCMethod**](QueryUnreceivedPacketsResponseIsTheResponseTypeForTheQueryUnreceivedPacketCommitmentsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_client_params**
> InlineResponse200104 ibc_core_client_v1_client_params()

ClientParams queries all parameters of the ibc client submodule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # ClientParams queries all parameters of the ibc client submodule.
    api_response = api_instance.ibc_core_client_v1_client_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_client_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_client_state**
> InlineResponse200102 ibc_core_client_v1_client_state(client_id)

ClientState queries an IBC light client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client state unique identifier

try:
    # ClientState queries an IBC light client.
    api_response = api_instance.ibc_core_client_v1_client_state(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_client_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client state unique identifier | 

### Return type

[**InlineResponse200102**](InlineResponse200102.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_client_states**
> InlineResponse200101 ibc_core_client_v1_client_states(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ClientStates queries all the IBC light clients of a chain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ClientStates queries all the IBC light clients of a chain.
    api_response = api_instance.ibc_core_client_v1_client_states(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_client_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_client_status**
> InlineResponse200103 ibc_core_client_v1_client_status(client_id)

Status queries the status of an IBC client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client unique identifier

try:
    # Status queries the status of an IBC client.
    api_response = api_instance.ibc_core_client_v1_client_status(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_client_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client unique identifier | 

### Return type

[**InlineResponse200103**](InlineResponse200103.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_consensus_state**
> QueryConsensusStateResponseIsTheResponseTypeForTheQueryConsensusStateRPCMethod ibc_core_client_v1_consensus_state(client_id, revision_number, revision_height, latest_height=latest_height)

ConsensusState queries a consensus state associated with a client state at a given height.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client identifier
revision_number = 'revision_number_example' # str | consensus state revision number
revision_height = 'revision_height_example' # str | consensus state revision height
latest_height = true # bool | latest_height overrrides the height field and queries the latest stored ConsensusState (optional)

try:
    # ConsensusState queries a consensus state associated with a client state at a given height.
    api_response = api_instance.ibc_core_client_v1_consensus_state(client_id, revision_number, revision_height, latest_height=latest_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_consensus_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client identifier | 
 **revision_number** | **str**| consensus state revision number | 
 **revision_height** | **str**| consensus state revision height | 
 **latest_height** | **bool**| latest_height overrrides the height field and queries the latest stored ConsensusState | [optional] 

### Return type

[**QueryConsensusStateResponseIsTheResponseTypeForTheQueryConsensusStateRPCMethod**](QueryConsensusStateResponseIsTheResponseTypeForTheQueryConsensusStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_consensus_state_heights**
> QueryConsensusStateHeightsResponseIsTheResponseTypeForTheQueryConsensusStateHeightsRPCMethod ibc_core_client_v1_consensus_state_heights(client_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ConsensusStateHeights queries the height of every consensus states associated with a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client identifier
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ConsensusStateHeights queries the height of every consensus states associated with a given client.
    api_response = api_instance.ibc_core_client_v1_consensus_state_heights(client_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_consensus_state_heights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client identifier | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryConsensusStateHeightsResponseIsTheResponseTypeForTheQueryConsensusStateHeightsRPCMethod**](QueryConsensusStateHeightsResponseIsTheResponseTypeForTheQueryConsensusStateHeightsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_consensus_states**
> QueryConsensusStatesResponseIsTheResponseTypeForTheQueryConsensusStatesRPCMethod ibc_core_client_v1_consensus_states(client_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

ConsensusStates queries all the consensus state associated with a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client identifier
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # ConsensusStates queries all the consensus state associated with a given client.
    api_response = api_instance.ibc_core_client_v1_consensus_states(client_id, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_consensus_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client identifier | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**QueryConsensusStatesResponseIsTheResponseTypeForTheQueryConsensusStatesRPCMethod**](QueryConsensusStatesResponseIsTheResponseTypeForTheQueryConsensusStatesRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_upgraded_client_state**
> InlineResponse200105 ibc_core_client_v1_upgraded_client_state()

UpgradedClientState queries an Upgraded IBC light client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # UpgradedClientState queries an Upgraded IBC light client.
    api_response = api_instance.ibc_core_client_v1_upgraded_client_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_upgraded_client_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_client_v1_upgraded_consensus_state**
> InlineResponse200106 ibc_core_client_v1_upgraded_consensus_state()

UpgradedConsensusState queries an Upgraded IBC consensus state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # UpgradedConsensusState queries an Upgraded IBC consensus state.
    api_response = api_instance.ibc_core_client_v1_upgraded_consensus_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_client_v1_upgraded_consensus_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_client_connections**
> QueryClientConnectionsResponseIsTheResponseTypeForTheQueryClientConnectionsRPCMethod ibc_core_connection_v1_client_connections(client_id)

ClientConnections queries the connection paths associated with a client state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
client_id = 'client_id_example' # str | client identifier associated with a connection

try:
    # ClientConnections queries the connection paths associated with a client state.
    api_response = api_instance.ibc_core_connection_v1_client_connections(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_client_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client identifier associated with a connection | 

### Return type

[**QueryClientConnectionsResponseIsTheResponseTypeForTheQueryClientConnectionsRPCMethod**](QueryClientConnectionsResponseIsTheResponseTypeForTheQueryClientConnectionsRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_connection**
> InlineResponse200108 ibc_core_connection_v1_connection(connection_id)

Connection queries an IBC connection end.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
connection_id = 'connection_id_example' # str | connection unique identifier

try:
    # Connection queries an IBC connection end.
    api_response = api_instance.ibc_core_connection_v1_connection(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| connection unique identifier | 

### Return type

[**InlineResponse200108**](InlineResponse200108.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_connection_client_state**
> QueryConnectionClientStateResponseIsTheResponseTypeForTheQueryConnectionClientStateRPCMethod ibc_core_connection_v1_connection_client_state(connection_id)

ConnectionClientState queries the client state associated with the connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
connection_id = 'connection_id_example' # str | connection identifier

try:
    # ConnectionClientState queries the client state associated with the connection.
    api_response = api_instance.ibc_core_connection_v1_connection_client_state(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_connection_client_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| connection identifier | 

### Return type

[**QueryConnectionClientStateResponseIsTheResponseTypeForTheQueryConnectionClientStateRPCMethod**](QueryConnectionClientStateResponseIsTheResponseTypeForTheQueryConnectionClientStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_connection_consensus_state**
> QueryConnectionConsensusStateResponseIsTheResponseTypeForTheQueryConnectionConsensusStateRPCMethod ibc_core_connection_v1_connection_consensus_state(connection_id, revision_number, revision_height)

ConnectionConsensusState queries the consensus state associated with the connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
connection_id = 'connection_id_example' # str | connection identifier
revision_number = 'revision_number_example' # str | 
revision_height = 'revision_height_example' # str | 

try:
    # ConnectionConsensusState queries the consensus state associated with the connection.
    api_response = api_instance.ibc_core_connection_v1_connection_consensus_state(connection_id, revision_number, revision_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_connection_consensus_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| connection identifier | 
 **revision_number** | **str**|  | 
 **revision_height** | **str**|  | 

### Return type

[**QueryConnectionConsensusStateResponseIsTheResponseTypeForTheQueryConnectionConsensusStateRPCMethod**](QueryConnectionConsensusStateResponseIsTheResponseTypeForTheQueryConnectionConsensusStateRPCMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_connection_params**
> InlineResponse200109 ibc_core_connection_v1_connection_params()

ConnectionParams queries all parameters of the ibc connection submodule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()

try:
    # ConnectionParams queries all parameters of the ibc connection submodule.
    api_response = api_instance.ibc_core_connection_v1_connection_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_connection_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ibc_core_connection_v1_connections**
> InlineResponse200107 ibc_core_connection_v1_connections(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

Connections queries all the IBC connections of a chain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # Connections queries all the IBC connections of a chain.
    api_response = api_instance.ibc_core_connection_v1_connections(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->ibc_core_connection_v1_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

